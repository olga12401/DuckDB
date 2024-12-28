import os
import duckdb
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

RAW_DIR = "/data"  # Directory where raw JSON files are stored
DB_PATH = "/duckdb_1/database/my_database.duckdb"  # DuckDB database file path
FLAG_FILE = "/duckdb_1/database/raw_data_complete.flag"  # Flag file to indicate completion

def load_raw_data():
    logging.info(f"Connecting to DuckDB database at '{DB_PATH}'...")
    conn = duckdb.connect(DB_PATH)

    for file_name in os.listdir(RAW_DIR):
        if file_name.endswith(".json"):
            table_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(RAW_DIR, file_name)
            logging.info(f"Loading data from '{file_path}' into table '{table_name}'...")
            try:
                conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_json_auto('{file_path}')")
                logging.info(f"Table '{table_name}' created successfully.")
            except Exception as e:
                logging.error(f"Error loading data into '{table_name}': {e}")

    logging.info("Raw data loading complete.")
    conn.close()

if __name__ == "__main__":
    try:
        load_raw_data()
        with open(FLAG_FILE, "w") as flag:
            flag.write("RAW_DATA_COMPLETE")
        logging.info(f"Flag file created: {FLAG_FILE}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)
