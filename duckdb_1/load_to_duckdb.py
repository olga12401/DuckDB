import os
import time
import duckdb

DATA_DIR = "/data"
DB_PATH = "/duckdb_1/my_database.duckdb"

# Ensure the database directory exists
if not os.path.exists(os.path.dirname(DB_PATH)):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def wait_for_files(directory, file_extension=".json", timeout=1500, interval=100):
    """
    Wait for files with the given extension to appear in the directory.
    :param directory: Directory to check for files.
    :param file_extension: File extension to wait for (default: ".json").
    :param timeout: Maximum wait time in seconds (default: 1500 seconds).
    :param interval: Time between checks in seconds (default: 100 seconds).
    """
    elapsed_time = 0
    while elapsed_time < timeout:
        files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
        if files:
            return files
        print(f"No {file_extension} files found in {directory}. Retrying in {interval} seconds...")
        time.sleep(interval)
        elapsed_time += interval
    raise TimeoutError(f"No {file_extension} files found in {directory} after {timeout} seconds.")

try:
    # Connect to DuckDB
    print(f"Connecting to DuckDB database at {DB_PATH}")
    con = duckdb.connect(DB_PATH)

    # Wait for JSON files to appear
    print(f"Waiting for JSON files in {DATA_DIR}...")
    json_files = wait_for_files(DATA_DIR)
    print(f"Found JSON files: {json_files}")

    # Load each JSON file into DuckDB
    for json_file in json_files:
        table_name = os.path.splitext(json_file)[0]
        json_path = os.path.join(DATA_DIR, json_file)

        print(f"Loading {json_file} into DuckDB table '{table_name}'...")
        try:
            query = f"CREATE TABLE {table_name} AS SELECT * FROM read_json_auto('{json_path}');"
            print(f"Running query: {query}")
            con.execute(query)
            print(f"Table '{table_name}' created successfully.")
        except Exception as e:
            print(f"Error loading {json_file}: {e}")

    print("All JSON files loaded into DuckDB.")
except TimeoutError as e:
    print(f"Timeout: {e}")
except Exception as e:
    print(f"Error loading data into DuckDB: {e}")

