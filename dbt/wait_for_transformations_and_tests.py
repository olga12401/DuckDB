import os
import time
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

STATUS_FILE = "/duckdb_1/raw_data_complete.flag"
FLAG_FILE_OUT = "/duckdb_1/dbt_complete.flag"

def wait_for_raw_data():
    """
    Wait for the raw data to be loaded into DuckDB.
    """
    while not os.path.exists(STATUS_FILE):
        logging.info("Waiting for raw data to be ready...")
        time.sleep(10)

def run_dbt():
    """
    Run DBT transformations and tests.
    """
    try:
        subprocess.run(["dbt", "run"], check=True)
        subprocess.run(["dbt", "test"], check=True)
        logging.info("DBT transformations and tests completed successfully.")

        # Create flag file to signal completion
        with open(FLAG_FILE_OUT, "w") as f:
            f.write("DBT_COMPLETE")
        logging.info(f"Flag file created: {FLAG_FILE_OUT}")

    except subprocess.CalledProcessError as e:
        logging.error(f"DBT command failed: {e}")
        exit(1)

if __name__ == "__main__":
    wait_for_raw_data()
    run_dbt()
