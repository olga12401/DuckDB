# DuckDB

## Structure 

1. [Introduction](#Introduction)
2. [Installation DuckDB](#Installation-DuckDB)
3. [Analyzing a CSV file with the DuckDB CLI](#Analyzing-a-CSV-file-with-the-DuckDB-CLI)
4. [Create a Database File](#Create-a-Database-File)
5. [Add tables to the database](#Add-tables-to-the-database)
6. [Reading a Parquet File in DuckDB](#Reading-a-Parquet-File-in-DuckDB)
7. [Accessing Files from Azure Blob Storage in DuckDB](#Accessing-Files-from-Azure-Blob-Storage-in-DuckDB)
8. [Project: MongoDB, DuckDB and DBT](#Project-MongoDB-DuckDB-and-DBT)
    - [Project Structure](#Project-Structure)

## Introduction 
This is simply an overview of the capabilities the DuckDB.

DuckDB is an open-source, in-process SQL database management system optimized for fast analytics and data processing. It is often described as an "SQLite for analytics" because of its lightweight, embeddable nature and its focus on handling analytical queries efficiently. DuckDB is designed to work well with columnar data, which makes it particularly suited for data science, machine learning, and other use cases involving large-scale data analysis.

The key features of DuckDB:

1. Analytical Focus
DuckDB is optimized for complex analytical queries (OLAP workloads) rather than transactional workloads (OLTP). It uses a columnar storage format, which makes it fast for scanning large datasets and performing operations like aggregations, joins, and filtering.
2. In-Process Database
DuckDB operates in-process, meaning it can run inside another application without requiring a separate database server. This allows it to be embedded directly within applications, data science environments, and ETL pipelines, similar to SQLite.
3. Easy Integration with Data Science Ecosystem
DuckDB integrates well with tools commonly used in data science, such as Python, R, and Apache Arrow. It can read data from various sources, including Parquet files, CSV files, and other data formats, without needing a data loading step.
4. SQL Support
DuckDB supports a rich subset of SQL, including complex analytical functions, window functions, and aggregations, making it versatile for many data processing tasks.
5. Performance
DuckDB is designed to be fast, leveraging vectorized query execution, which processes data in chunks to take advantage of modern CPUs. It can perform well with both in-memory and disk-based queries and can scale effectively for larger datasets.
6. Concurrency and ACID Compliance
Although primarily focused on analytics, DuckDB supports ACID transactions, and it can handle concurrent read operations, making it reliable and suitable for multi-user environments.
7. Deployment and Usage
DuckDB can be used on personal computers, servers, and in cloud environments. It is often used directly from within programming languages (e.g., using a Python or R API) or command-line interfaces.
Typical Use Cases
Exploratory Data Analysis: DuckDB is ideal for data scientists who need a quick way to query and explore datasets.
ETL Pipelines: Its ability to read data in various formats makes it useful in data transformation pipelines.
Data Lake Querying: With support for file formats like Parquet, DuckDB can act as a simple yet powerful query engine on data lakes.
Overall, DuckDB provides a compelling combination of SQL compatibility, speed, and ease of integration with the data science workflow, making it increasingly popular in analytics-driven fields.

## Installation DuckDB 

### On MAC

```
brew install duckdb
```

### On The Linux /  WSL Ubuntu Terminal on the Windows

1. Download the latest Linux version of the DuckDB CLI. Try this command (this URL is subject to change if DuckDB releases a newer version):

```
wget https://github.com/duckdb/duckdb/releases/download/v1.1.3/duckdb_cli-linux-amd64.zip
```

2. Unzip the Linux version you downloaded:

```
unzip duckdb_cli-linux-amd64.zip

```

3. Move the Executable to Your PATH and Make It Executable

```
sudo mv duckdb /usr/local/bin/
sudo chmod +x /usr/local/bin/duckdb

```

4. Verify Installation

Run the following command to verify that DuckDB is correctly installed:

```
duckdb

```
5.  Check for the DuckDB Prompt: If DuckDB is correctly installed, you should see a prompt that looks something like this:

```
v1.1.3 19864453f7
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D 
```

To return from .mode duckbox, use the command ```Ctrl + Z```.
To get a list of the available CLI arguments, run the command  ```duckdb -help```.

DuckDB cannot query files that live elsewhere on the internet, but that capability is available via the official httpfs extension. If it is not already in your distribution, you can install and load the httpfs extension. This extension lets us directly query files hosted on an HTTP(S) server without having to download the files locally, it also supports S3 and some other cloud storage providers.

``` 
INSTALL httpfs;
LOAD httpfs;
```
<img width="606" alt="image" src="https://github.com/user-attachments/assets/d903c7db-a81a-4904-81c7-1dcf08a9032c">

##  Analyzing a CSV file with the DuckDB CLI

It doesn’t matter where our data is stored, be it on a remote HTTP server or cloud storage (S3, GCP, HDFS), DuckDB can process it now directly without having to do a manual download and import process. If, as is the case here, our URL or file name ends in a specific extension (e.g. .csv), DuckDB will automatically process it.
To Run the command in the duckbox.
```
SELECT count(*)
FROM 'https://github.com/bnokoro/Data-Science/raw/master/countries%20of%20the%20world.csv';

```
<img width="592" alt="image-2" src="https://github.com/user-attachments/assets/1edad318-bbe6-4732-8d4d-1fe0979545d7">

##  Create a Database File

1. To create a database in DuckDB , specify the database filename when launching DuckDB, or use the ```ATTACH DATABASE``` command. 
DuckDB will automatically create a new database if the file doesn’t exist.

In your terminal, create and open a new, empty DuckDB database by specifying a filename when launching DuckDB.
This command will create an empty database file named my_database.db in the current directory if it doesn’t already exist. If it already exists, DuckDB will open it without overwriting the data.
```
duckdb my_database.db
```
2. Verify the Empty Database

```
.tables
```

3. Exit DuckDB 
If you just wanted to create an empty database without adding tables or data right now, you can exit DuckDB by typing:
```
.exit
```

##  Add tables to the database

1. Open the Database ```duckdb my_database.db```
2. Create a Table

```
CREATE TABLE orders (
      order_id INTEGER PRIMARY KEY,          -- Unique ID for each order
      customer_id INTEGER,                   -- ID referencing the customer
      order_date DATE,                       -- Date when the order was placed
      shipping_date DATE,                    -- Date when the order is scheduled to ship
      total_amount DECIMAL(10, 2),           -- Total amount of the order
      status VARCHAR,                        -- Status of the order (e.g., 'Pending', 'Shipped', 'Delivered', 'Cancelled')
      payment_method VARCHAR,                -- Payment method used (e.g., 'Credit Card', 'PayPal', 'Cash')
      shipping_address VARCHAR,              -- Shipping address for the order
      billing_address VARCHAR                -- Billing address for the order
  );

```
3. Insert Sample Data into the `orders` Table

```
INSERT INTO orders VALUES
(1001, 1, '2023-10-05', '2023-10-07', 150.75, 'Shipped', 'Credit Card', '123 Elm St, Springfield', '123 Elm St, Springfield'),
(1002, 2, '2023-10-06', '2023-10-08', 299.99, 'Pending', 'PayPal', '456 Oak St, Riverside', '456 Oak St, Riverside'),
(1003, 1, '2023-10-07', '2023-10-09', 89.50, 'Delivered', 'Credit Card', '123 Elm St, Springfield', '123 Elm St, Springfield'),
(1004, 3, '2023-10-08', NULL, 49.95, 'Cancelled', 'Cash', '789 Pine St, Meadowview', '789 Pine St, Meadowview');

```
4. Query the `orders` Table to Verify

```
SELECT * FROM orders;
```

<img width="890" alt="image-3" src="https://github.com/user-attachments/assets/3dfccbe5-e970-4ce4-993b-7d05cfb74433">

## Reading a Parquet File in DuckDB

DuckDB can read and write Parquet files directly, allowing you to use Parquet files as a data source or to export DuckDB tables into Parquet format.
To read a Parquet file in DuckDB, you can use the `read_parquet` function to treat it as a virtual table or load it into a DuckDB table for further processing.
1. Reading Parquet Data as a Virtual Table

If you want to query the Parquet file directly without importing it into a DuckDB table, you can do the following:

```
SELECT * FROM read_parquet('path/to/your_file.parquet');

```
<img width="654" alt="image-4" src="https://github.com/user-attachments/assets/d9373a2c-636d-4fae-bf06-0d5636b4101d">

2. Creating a Table from Parquet Data

If you want to load the data from a Parquet file into a DuckDB table:
```
CREATE TABLE my_table AS SELECT * FROM read_parquet('path/to/mtcars.parquet');
SELECT * FROM my_table;
```
This will create a new table my_table in DuckDB and load the data from the Parquet file into it.

To check how many tables exist in your DuckDB database, you can query the `information_schema.tables` system table, which stores metadata about tables.

```
SELECT table_name FROM information_schema.tables WHERE table_schema = 'main';

```
<img width="461" alt="image-5" src="https://github.com/user-attachments/assets/946defb7-0150-4723-951d-9f0b40c171c2">

3. Writing Data to a Parquet File

You can also export data from a DuckDB table to a Parquet file. For example, if you want to save the `orders` table as a Parquet file:
```
COPY orders TO 'path/data/orders.parquet' (FORMAT PARQUET);

```

## Accessing Files from Azure Blob Storage in DuckDB

1. Set Up Azure Blob Storage and Generate SAS Token

  - Log in to Azure Portal.
  - Create a Storage Account (if you don't have one already). Go to Storage Accounts > Create and set up your storage account.
  - Create a Container in Blob Storage.
  - Upload Your File to the Container.
  - Generate a Shared Access Signature (SAS) Token:
      - In the storage account menu, find and select Shared access signature under the `Security + networking` section on the left-hand side. This page will allow you to configure and generate a SAS token for accessing your storage account resources.
      - `Set Permissions`. Under Allowed permissions, check the following permissions:
          * `Read`: Allows reading of the blob content (this is required to access your data).
          * `List`: (Optional but recommended) Allows listing the contents of a container. Useful if you want to access multiple files or see file contents in the container.
      - `Allowed Resource Types`. Check `Container` and `Object`. This will allow access to both the container (to list its contents) and the individual blobs (to read specific files).
      - `Specify the Start and Expiry Date`. 
          * Set the `Start date and time` (optional). You can set it to the current date and time or leave it blank to activate immediately.
          * Set an `Expiry date and time` for when the SAS token should expire. Make sure to choose an appropriate expiration date based on how long you need access.
      - `Allowed Protocols`. Choose `HTTPS only` for security (recommended).
      - `Allowed IP Addresses` (Optional). You can restrict the SAS token to specific IP addresses. If you’re testing or accessing it from a known IP range, you can add it here for extra security.
      - `Allowed IP Addresses` (Optional). You can restrict the SAS token to specific IP addresses. If you’re testing or accessing it from a known IP range, you can add it here for extra security.

    <img width="878" alt="blob" src="https://github.com/user-attachments/assets/b8a71ff9-fc43-4a1e-9d8e-1ba105315f46">

      - `Generate SAS and connection string` at the bottom of the page.
      - After generating, you’ll see two important values:
        * `SAS Token`: This is the token you’ll add to your URLs in DuckDB.
        * `Blob service SAS URL`: This is the URL for your container, with the SAS token appended. You can use this URL directly if accessing the entire container or individual files within it.
    - Copy the SAS Token string (it starts with `?sv=...`) or the Blob service SAS URL.

### Integration the SAS Token into DuckDB

1. Set Up DuckDB to Access Azure Blob Storage.  Start DuckDB and Load the `httpfs` Extension.

The `httpfs` extension is required to access files over HTTP/HTTPS.
```
INSTALL httpfs;
LOAD httpfs;
```
2. Configure your Azure storage account name and SAS token as settings in DuckDB.

```
SET azure_storage.account_name = 'your_account_name';
SET azure_storage.sas_token = 'your_sas_token';
```
However, we can get en error, because the DuckDB’s `httpfs` extension, while supporting S3 and GCS storage, does not yet directly support Azure-specific configurations in the same way (as of the latest release). So we can construct the `Full URL with SAS Token`

```
https://<your_account_name>.blob.core.windows.net/<container_name>/<file_name>?<sas_token>

```
Replace <your_account_name>, <container_name>, <file_name>, and <sas_token> with your actual values.

3. Read the File Directly from the Azure Blob URL.

Use the `read_parquet` or `read_csv_auto` function with the full URL (including the SAS token) to access your file.

```
SELECT * FROM read_csv_auto('https://<your_account_name>.blob.core.windows.net/<container_name>/<file_name>?<sas_token>');

SELECT * FROM read_parquet('https://<your_account_name>.blob.core.windows.net/<container_name>/<file_name>?<sas_token>');

```

4. Create a Table in DuckDB from the Azure Blob Storage Data.

```
CREATE TABLE name_table AS SELECT * FROM read_csv_auto('https://<your_account_name>.blob.core.windows.net/<container_name>/<file_name>?<sas_token>');

CREATE TABLE name_table AS SELECT * FROM read_parquet('https://<your_account_name>.blob.core.windows.net/<container_name>/<file_name>?<sas_token>');
```
5. Verify the Table Creation.
```
SELECT * FROM name_table LIMIT 10;
```

<img width="670" alt="blob2" src="https://github.com/user-attachments/assets/ac1b182f-dd3b-4af4-86aa-120f3ef51586">

## Project MongoDB, DuckDB and DBT  

This project represents a data engineering pipeline for extracting, transforming, and analyzing data, specifically using MongoDB, DuckDB, and DBT (Data Build Tool). Below is a detailed explanation of the project structure and its components:

### Directory Structure
```

project/
├── data/
│   ├── raw/                 # Directory for raw JSON data fetched from MongoDB
│   ├── transformed/         # Directory for transformed data (output from DBT)
├── mongodb/
│   ├── .env                 # Environment variables for MongoDB connection
│   ├── Dockerfile           # Dockerfile to build the MongoDB fetcher image
│   ├── fetch_data.py        # Script to fetch data from MongoDB
│   ├── requirements.txt     # Python dependencies for the fetcher
├── duckdb_1/
│   ├── database/            # Directory for DuckDB database files
│   ├── Dockerfile           # Dockerfile to build the DuckDB loader image
│   ├── load_to_duckdb.py    # Script to load raw data into DuckDB
│   ├── load_transformed_to_duckdb.py # Script to load transformed data into DuckDB
├── dbt/
│   ├── Dockerfile           # Dockerfile to build the DBT image
│   ├── dbt_project.yml      # DBT project configuration
│   ├── profiles.yml         # DBT profile configuration for DuckDB
│   ├── wait_for_transformations_and_tests.py # Script to run DBT and wait for tests
│   ├── models/
│   │   ├── test/
│   │   │   └── users_comments.sql # DBT test to verify data validity
│   │   ├── transformed/
│   │   │   ├── schema.yml   # DBT schema for transformed data
│   │   │   └── users_comments.sql # SQL model for users' activity transformation
├── docker-compose.yml       # Docker Compose file for orchestrating services



```

### Project Structure

1. ```mongodb/```: Handles data extraction from MongoDB and saves data into JSON files.
2. ```duckdb_1/```: Manages data loading and transformations within DuckDB.
3. ```dbt/```: Applies advanced transformations, schema validations, and tests using DBT.

### Detailed Explanation

1. ```mongodb/```
Purpose: Fetch raw data from MongoDB and save it as JSON files.

- ```dockerfile:```

  - Uses ```python:3.9-slim``` to create a lightweight container.
  - Installs dependencies from ```requirements.txt```.
  - Runs the ```fetch_data.py``` script.

- ```fetch_data.py:```

   - Connects to MongoDB using credentials from ```.env```.
   - Serializes data from MongoDB collections (```users```, ```movies```, ```comments```) into JSON format.
   - Saves the data into the directory specified by ```DATA_DIR```.
   - ```.env```: Contains sensitive connection details (MongoDB URI, database name, data directory path).

- ```requirements.txt```: Specifies dependencies: ```pymongo``` (MongoDB driver) and ```python-dotenv``` (to load ```.env``` variables).

2. ```duckdb_1/```

Purpose: Load the extracted JSON data into DuckDB and manage schema-level transformations.

- ```dockerfile```:

   - Uses ```python:3.9-slim``` as the base image.
   - Installs ```duckdb``` for database management.
   - Runs the ```load_to_duckdb.py``` script by default.

- ```load_to_duckdb.py```:

   - Monitors the ```/data``` directory for JSON files.
   - Loads the JSON data into DuckDB as individual tables.
   - Creates a flag file (```raw_data_complete.flag```) to signal data availability.
- ```load_transformed_to_duckdb.py```:

   - Waits for a flag (```dbt_complete.flag```) to indicate that DBT transformations are complete.

3. ```dbt/```

Purpose: Transform raw data and validate with DBT.

- ```Dockerfile```:
   - Base Image: Uses ```python:3.9-slim```.
   - Dependencies:
     - Installs ```dbt-core``` and ```dbt-duckdb``` for transformation and validation.
     - Installs ```git``` for managing DBT dependencies.
   -Default Command: Runs ```wait_for_transformations_and_tests.py```.

- ```dbt_project.yml```:
Purpose:
Configures the DBT project.
Specifies schemas for raw (raw) and transformed (transformed) models.
```
name: 'duckdb_project'
version: '1.0.0'

profile: 'duckdb'

config-version: 2

model-paths: ["models"]

models:
  duckdb_project:
    raw:
      +schema: raw
    transformed:
      +schema: transformed
```

- ```profiles.yml```:
Purpose: Configures DBT to connect to the DuckDB database.
```
duckdb:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: /duckdb_1/database/my_database.duckdb
      threads: 1

```

- ```wait_for_transformations_and_tests.py```:
Functionality:
   - Waits for the flag file (```raw_data_complete.flag```) indicating raw data loading.

```
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
```

