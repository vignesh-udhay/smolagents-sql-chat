from smolagents import tool
from sqlalchemy import text
from db import engine

def get_table_data():
    """Get all data from the receipts table in a format suitable for display."""
    with engine.connect() as con:
        result = con.execute(text("SELECT * FROM receipts"))
        rows = result.fetchall()
        return [list(row) for row in rows]

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - receipt_id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output 