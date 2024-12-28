FROM python:3.9-slim

WORKDIR /dbt

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir dbt-core==1.5.2 dbt-duckdb==1.5.2

COPY . .

CMD ["python", "wait_for_transformations_and_tests.py"]

