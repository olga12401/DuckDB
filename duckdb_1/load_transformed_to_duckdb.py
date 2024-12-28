import duckdb
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DB_PATH = "/duckdb_1/database/my_database.duckdb"  # DuckDB database file path
TRANSFORMED_TABLE = "main_transformed.users_comments"  # Transformed DBT table
TARGET_TABLE = "users_comments"  # Target table in DuckDB
FLAG_FILE = "/duckdb_1/database/dbt_complete.flag"  # Flag file to indicate completion

def ensure_table():
    """
    Ensure that the target table exists. If it doesn't, create it using the structure
    of the transformed table, but without any data.
    """
    logging.info(f"Ensuring the '{TARGET_TABLE}' table exists...")
    conn = duckdb.connect(DB_PATH)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {TARGET_TABLE} AS
        SELECT * FROM {TRANSFORMED_TABLE} WHERE FALSE;
    """)
    logging.info(f"Table '{TARGET_TABLE}' is ready.")
    conn.close()

def load_transformed_data():
    """
    Load data from the transformed DBT table into the target table.
    """
    logging.info(f"Loading data from '{TRANSFORMED_TABLE}' into '{TARGET_TABLE}'...")
    conn = duckdb.connect(DB_PATH)
    conn.execute(f"INSERT INTO {TARGET_TABLE} SELECT * FROM {TRANSFORMED_TABLE};")
    logging.info(f"Data successfully loaded into '{TARGET_TABLE}'.")
    conn.close()

def create_flag():
    """
    Create a flag file to indicate successful loading of transformed data.
    """
    logging.info(f"Creating flag file: {FLAG_FILE}")
    with open(FLAG_FILE, "w") as flag:
        flag.write("DBT_COMPLETE")
    logging.info(f"Flag file '{FLAG_FILE}' created successfully.")

if __name__ == "__main__":
    try:
        logging.info(f"Connecting to DuckDB database at '{DB_PATH}'...")
        ensure_table()
        load_transformed_data()
        create_flag()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)