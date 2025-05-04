# SmolAgent Text-to-SQL

A natural language interface for querying a SQL database using AI. This application allows users to ask questions about receipt data in plain English and get SQL-powered responses.

## Features

- Natural language interface for database queries
- Real-time table visualization
- Powered by Groq's Llama 3.3 70B model
- Simple and intuitive Gradio web interface

## Prerequisites

- Python 3.8+
- Groq API key

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd smolagent-text-to-sql
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Initialize the database:

```bash
python init_db.py
```

2. Start the application:

```bash
python app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (typically http://127.0.0.1:7860)

4. Ask questions about the receipts data in natural language, such as:
   - "Who had the most expensive receipt?"
   - "What was the average tip amount?"
   - "Show me all receipts above $20"

## Database Schema

The application uses a simple receipts table with the following structure:

| Column        | Type    | Description     |
| ------------- | ------- | --------------- |
| receipt_id    | Integer | Primary key     |
| customer_name | String  | Customer's name |
| price         | Float   | Receipt amount  |
| tip           | Float   | Tip amount      |

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
