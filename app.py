import os

import gradio as gr
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel

from init_db import init_database
from tools import get_table_data, sql_engine

# Load environment variables
load_dotenv()

# Initialize the database
init_database()

api_key = os.getenv("GROQ_API_KEY")

model = LiteLLMModel(
    model_id="llama-3.3-70b-versatile",
    api_base="https://api.groq.com/openai/v1",
    api_key=api_key,
    flatten_messages_as_text=True
)

# Initialize the agent with Groq's Mixtral model
agent = CodeAgent(
    tools=[sql_engine],
    model= model
    # uncomment the line below to use Qwen/Qwen2.5-Coder-32B-Instruct from huggingface
    # model=InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")
)

def process_query(query):
    """Process the user query and return the response."""
    system_prompt = """You are a helpful SQL assistant that provides responses in a friendly, conversational manner. 
    When answering questions about the receipts data, explain your findings in a clear and natural way.
    If you need to show data, present it in a readable format and explain what it means.
    Be concise but informative in your responses."""
    
    full_query = f"{system_prompt}\n\nUser: {query}"
    response = agent.run(full_query)
    return response, ""

def get_table():
    """Get the current state of the table."""
    rows = get_table_data()
    headers = ["Receipt ID", "Customer Name", "Price", "Tip"]
    return gr.DataFrame(
        value=rows,
        headers=headers,
        datatype=["number", "str", "number", "number"],
        row_count=len(rows),
        col_count=4,
    )

with gr.Blocks(title="SQL Query Assistant") as demo:
    gr.Markdown("# SQL Query Assistant")
    gr.Markdown("Ask questions about the receipts data in natural language.")
    
    with gr.Row():
        with gr.Column(scale=2):
            table = gr.DataFrame(
                headers=["Receipt ID", "Customer Name", "Price", "Tip"],
                datatype=["number", "str", "number", "number"],
                row_count=4,
                col_count=4,
            )
        
        with gr.Column(scale=3):
            response = gr.Textbox(label="Response", lines=10)
            query = gr.Textbox(
                label="Ask a question",
                placeholder="e.g., Who had the most expensive receipt?",
            )
            submit_btn = gr.Button("Submit")
    
    submit_btn.click(
        fn=process_query,
        inputs=[query],
        outputs=[response, query],
    ).then(
        fn=get_table,
        outputs=table,
    )
    
    # Initialize the table
    demo.load(fn=get_table, outputs=table)

if __name__ == "__main__":
    demo.launch() 