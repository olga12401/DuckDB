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
    conn.execute(f"CREATE TABLE IF NOT EXISTS {TARGET_TABLE} AS SELECT * FROM {TRANSFORMED_TABLE} WHERE FALSE;")
  

