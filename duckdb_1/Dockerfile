FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install duckdb

# Ensure the database directory exists
RUN mkdir -p /duckdb_1/database

COPY load_to_duckdb.py .
COPY load_transformed_to_duckdb.py .

CMD ["python", "load_to_duckdb.py"]
