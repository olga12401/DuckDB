import os
import duckdb
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

RAW_DIR = "/data"
DB_DIR = "/duckdb_1/database"
DB_PATH = f"{DB_DIR}/my_database.duckdb"
FLAG_FILE = f"{DB_DIR}/raw_data_complete.flag"
WAIT_TIMEOUT = 60  # Maximum wait time in seconds

def ensure_directory_exists(directory):
    """
    Ensure that the directory exists, creating it if necessary.
    """
    if not os.path.exists(directory):
        logging.info(f"Directory '{directory}' does not exist. Creating it...")
        os.makedirs(directory)
        logging.info(f"Directory '{directory}' created.")

def ensure_database_exists():
    """
    Ensure the DuckDB database file exists.
    """
    if not os.path.exists(DB_PATH):
        logging.info(f"Database file '{DB_PATH}' does not exist. Creating a new one.")
        conn = duckdb.connect(DB_PATH)
        conn.close()
        logging.info(f"Database '{DB_PATH}' created successfully.")

def load_raw_data():
    """
    Load raw data JSON files into the DuckDB database.
    """
    ensure_directory_exists(DB_DIR)
    ensure_database_exists()
    logging.info(f"Connecting to DuckDB database at '{DB_PATH}'...")
    conn = duckdb.connect(DB_PATH)

    for file_name in os.listdir(RAW_DIR):
        if file_name.endswith(".json"):
            table_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(RAW_DIR, file_name)
            logging.info(f"Loading data from '{file_path}' into table '{table_name}'...")
            conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_json_auto('{file_path}')")

    logging.info("Raw data loading complete.")
    conn.close()

if __name__ == "__main__":
    try:
        ensure_directory_exists(DB_DIR)
        load_raw_data()
        with open(FLAG_FILE, "w") as flag:
            flag.write("RAW_DATA_COMPLETE")
        logging.info(f"Flag file created: {FLAG_FILE}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)
