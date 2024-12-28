import os
import duckdb
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TRANSFORMED_DIR = "/data/transformed"
DB_PATH = "/duckdb_1/my_database.duckdb"
NEW_SCHEMA = "analytics"
FLAG_FILE_IN = "/duckdb_1/dbt_complete.flag"

def wait_for_flag(flag_file, timeout=1500, interval=10):
    """
    Wait for a flag file to indicate readiness.
    """
    elapsed_time = 0
    while elapsed_time < timeout:
        if os.path.exists(flag_file):
            logging.info(f"Flag file '{flag_file}' detected.")
            return
        logging.info(f"Waiting for flag file '{flag_file}'...")
        time.sleep(interval)
        elapsed_time += interval
    raise TimeoutError(f"Timeout waiting for flag file '{flag_file}'.")

try:
    # Wait for DBT to complete its transformations
    wait_for_flag(FLAG_FILE_IN)

    con = duckdb.connect(DB_PATH)
    con.execute(f"CREATE SCHEMA IF NOT EXISTS {NEW_SCHEMA};")
    logging.info(f"Schema '{NEW_SCHEMA}' created.")

    for file in os.listdir(TRANSFORMED_DIR):
        if file.endswith(".csv"):
            table_name = os.path.splitext(file)[0]
            file_path = os.path.join(TRANSFORMED_DIR, file)

            con.execute(f"""
                CREATE OR REPLACE TABLE {NEW_SCHEMA}.{table_name} AS 
                SELECT * FROM read_csv_auto('{file_path}');
            """)
            logging.info(f"Loaded table '{NEW_SCHEMA}.{table_name}'.")

except Exception as e:
    logging.error(f"An error occurred: {e}")
