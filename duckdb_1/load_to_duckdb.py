import os
import time
import duckdb
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DATA_DIR = "/data"  # Directory where raw JSON files are stored
DB_PATH = "/duckdb_1/my_database.duckdb"  # Path to DuckDB database file
MONGODB_FLAG_FILE = "/data/mongodb_fetch_complete.flag"  # MongoDB fetch completion flag
RAW_FLAG_FILE = "/duckdb_1/raw_data_complete.flag"  # Raw data loading completion flag

def wait_for_flag(flag_file, timeout=600, interval=10):
    """
    Wait for a flag file to be created.
    :param flag_file: Path to the flag file
    :param timeout: Maximum wait time in seconds (default: 10 minutes)
    :param interval: Check interval in seconds (default: 10 seconds)
    :raises TimeoutError: If the flag file is not found within the timeout
    """
    logging.info(f"Waiting for flag file '{flag_file}'...")
    elapsed_time = 0
    while elapsed_time < timeout:
        if os.path.exists(flag_file):
            logging.info(f"Flag file '{flag_file}' detected.")
            return
        time.sleep(interval)
        elapsed_time += interval
    raise TimeoutError(f"Timeout waiting for flag file '{flag_file}'.")

def create_duckdb_directory(db_path):
    """
    Ensure the directory for the DuckDB database exists.
    :param db_path: Path to the DuckDB database file
    """
    db_directory = os.path.dirname(db_path)
    if not os.path.exists(db_directory):
        logging.info(f"Directory '{db_directory}' does not exist. Creating it.")
        os.makedirs(db_directory, exist_ok=True)

def load_json_to_duckdb(con, data_dir, json_files):
    """
    Load JSON files into DuckDB tables.
    :param con: DuckDB connection object
    :param data_dir: Directory containing JSON files
    :param json_files: List of JSON filenames to process
    """
    for json_file in json_files:
        table_name = os.path.splitext(json_file)[0]  # Use the file name (without extension) as the table name
        file_path = os.path.join(data_dir, json_file)

        if os.path.exists(file_path):
            logging.info(f"Loading {json_file} into table '{table_name}'...")
            try:
                query = f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_json_auto('{file_path}');"
                con.execute(query)
                logging.info(f"Table '{table_name}' created successfully.")
            except Exception as e:
                logging.error(f"Failed to load {json_file}: {e}")
        else:
            logging.warning(f"File {file_path} does not exist. Skipping.")

try:
    # Wait for MongoDB fetch completion flag
    wait_for_flag(MONGODB_FLAG_FILE)

    # Ensure DuckDB directory exists
    create_duckdb_directory(DB_PATH)

    # Connect to DuckDB
    logging.info(f"Connecting to DuckDB database at {DB_PATH}")
    con = duckdb.connect(DB_PATH)

    # List of JSON files to process
    json_files = ["users.json", "movies.json", "comments.json"]

    # Load data from JSON files into DuckDB
    load_json_to_duckdb(con, DATA_DIR, json_files)

    # Create a flag file to signal completion
    with open(RAW_FLAG_FILE, "w") as f:
        f.write("RAW_DATA_LOADED")
    logging.info(f"Flag file created: {RAW_FLAG_FILE}")

except TimeoutError as e:
    logging.error(f"Timeout error: {e}")
    exit(1)
except Exception as e:
    logging.error(f"An error occurred: {e}")
    exit(1)
