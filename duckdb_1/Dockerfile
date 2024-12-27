FROM python:3.9-slim

WORKDIR /app

RUN pip install duckdb

COPY load_to_duckdb.py .

CMD ["python", "load_to_duckdb.py"]
