# DuckDB

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

## Instalation DuckDB 

### On MAC

´´´
brew install duckdb
´´´

### On The Linux /  WSL Ubuntu Terminal on the Windows

1. Download the latest Linux version of the DuckDB CLI. Try this command (this URL is subject to change if DuckDB releases a newer version):

´´´
wget https://github.com/duckdb/duckdb/releases/download/v1.1.3/duckdb_cli-linux-amd64.zip
´´´

2. Unzip the Linux version you downloaded:

´´´
unzip duckdb_cli-linux-amd64.zip

´´´

3. Move the Executable to Your PATH and Make It Executable

´´´
sudo mv duckdb /usr/local/bin/
sudo chmod +x /usr/local/bin/duckdb

´´´

4. Verify Installation

Run the following command to verify that DuckDB is correctly installed:

´´´
duckdb

´´´
5.  Check for the DuckDB Prompt: If DuckDB is correctly installed, you should see a prompt that looks something like this:

v1.1.3 19864453f7
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D 

To return from .mode duckbox, use the command ´´´Ctrl + Z´´´.
To get a list of the available CLI arguments, run the command  ´´´duckdb -help´´´.

DuckDB cannot query files that live elsewhere on the internet, but that capability is available via the official httpfs extension. If it is not already in your distribution, you can install and load the httpfs extension. This extension lets us directly query files hosted on an HTTP(S) server without having to download the files locally, it also supports S3 and some other cloud storage providers.

´´´
INSTALL httpfs;
LOAD httpfs;
´´´
![alt text](image.png)

##  Analyzing a CSV file with the DuckDB CLI

It doesn’t matter where our data is stored, be it on a remote HTTP server or cloud storage (S3, GCP, HDFS), DuckDB can process it now directly without having to do a manual download and import process. If, as is the case here, our URL or file name ends in a specific extension (e.g. .csv), DuckDB will automatically process it.
To Run the command in the duckbox.
´´´
SELECT count(*)
FROM 'https://github.com/bnokoro/Data-Science/raw/master/countries%20of%20the%20world.csv';

´´´
![alt text](image-2.png)

