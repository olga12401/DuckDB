# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the fetch_data script
COPY fetch_data.py .
COPY .env /app/.env

# Set the default command
CMD ["python", "fetch_data.py"]

