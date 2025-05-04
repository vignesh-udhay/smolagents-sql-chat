from sqlalchemy import (Column, Float, Integer, MetaData, String, Table,
                        insert, inspect)
from db import engine
from sqlalchemy.sql import text

def init_database():
    """Initialize the database with the receipts table and sample data."""
    try:
        metadata_obj = MetaData()

        # Create the table
        table_name = "receipts"
        receipts = Table(
            table_name,
            metadata_obj,
            Column("receipt_id", Integer, primary_key=True),
            Column("customer_name", String(16), primary_key=True),
            Column("price", Float),
            Column("tip", Float),
        )
        
        # Drop the table if it exists to ensure clean state
        with engine.connect() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
            conn.commit()
        
        # Create the table
        metadata_obj.create_all(engine)

        # Insert sample data
        rows = [
            {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
            {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
            {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
            {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
        ]
        
        for row in rows:
            stmt = insert(receipts).values(**row)
            with engine.begin() as connection:
                connection.execute(stmt)
                
        print("Database initialized successfully!")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

if __name__ == "__main__":
    init_database() 