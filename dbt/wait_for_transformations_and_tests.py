import os
import time
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DBT_COMMANDS = [
    ["dbt", "run"],
    ["dbt", "test"]
]

RAW_DATA_FLAG = "/duckdb_1/database/raw_data_complete.flag"
TRANSFORMED_FLAG = "/duckdb_1/database/dbt_complete.flag"

def wait_for_flag(flag_path, check_interval=5):
    """
    Wait for a specified flag file to be created.
    """
    logging.info(f"Waiting for flag file '{flag_path}'...")
    while not os.path.exists(flag_path):
        time.sleep(check_interval)
    logging.info(f"Flag file '{flag_path}' detected.")

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
        run_dbt_commands()
        with open(TRANSFORMED_FLAG, "w") as flag:
            flag.write("DBT_TRANSFORMATIONS_COMPLETE")
        logging.info(f"Flag file created: {TRANSFORMED_FLAG}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)
