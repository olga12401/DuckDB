import os
import time
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

RAW_DATA_FLAG = "/duckdb_1/database/raw_data_complete.flag"
TRANSFORMED_FLAG = "/duckdb_1/database/dbt_complete.flag"
TRANSFORMED_DIR = "/data/transformed"

DBT_COMMANDS = [
    ["dbt", "run"],
    ["dbt", "test"]
]

def wait_for_flag(flag_path, timeout=600, interval=5):
    """
    Wait for a specified flag file to be created, with a timeout.
    """
    logging.info(f"Waiting for flag file '{flag_path}'...")
    elapsed_time = 0
    while not os.path.exists(flag_path):
        time.sleep(interval)
        elapsed_time += interval
        if elapsed_time >= timeout:
            raise TimeoutError(f"Timeout waiting for flag file '{flag_path}'.")
    logging.info(f"Flag file '{flag_path}' detected.")

def ensure_transformed_directory():
    """
    Ensure that the transformed directory exists and is ready.
    """
    logging.info(f"Checking transformed directory: '{TRANSFORMED_DIR}'")
    if not os.path.exists(TRANSFORMED_DIR):
        os.makedirs(TRANSFORMED_DIR)
        logging.info(f"Created transformed directory: '{TRANSFORMED_DIR}'")

def run_dbt_commands():
    """
    Execute the DBT commands (run and test).
    """
    for command in DBT_COMMANDS:
        logging.info(f"Running DBT command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"DBT command failed: {result.stderr}")
            raise Exception(f"DBT command failed: {result.stderr}")
        logging.info(result.stdout)

if __name__ == "__main__":
    try:
        wait_for_flag(RAW_DATA_FLAG)
        ensure_transformed_directory()
        run_dbt_commands()
        with open(TRANSFORMED_FLAG, "w") as flag:
            flag.write("DBT_TRANSFORMATIONS_COMPLETE")
        logging.info(f"Flag file created: {TRANSFORMED_FLAG}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)
