# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /dbt

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install DBT Core and DBT-DuckDB
RUN pip install --no-cache-dir dbt-core==1.5.2 dbt-duckdb==1.5.2

# Copy the entire DBT project into the container
COPY . .

# Set the default command to execute DBT tasks
CMD ["python", "wait_for_transformations_and_tests.py"]

