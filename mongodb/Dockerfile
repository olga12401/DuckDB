# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the data fetch script into the container
COPY fetch_data.py .

# Set the default command to execute the fetch_data.py script
CMD ["python", "fetch_data.py"]
