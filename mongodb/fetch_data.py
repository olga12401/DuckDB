import os
import json
import datetime
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Environment variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "sample_mflix")
DATA_DIR = os.getenv("DATA_DIR", "/data")
FLAG_FILE = os.path.join(DATA_DIR, "mongodb_fetch_complete.flag")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Custom serializer for MongoDB objects
def serialize(obj):
    """
    Custom serializer for MongoDB objects.
    """
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

try:
    # Connect to MongoDB
    logging.info("Connecting to MongoDB...")
    client = MongoClient(MONGO_URI)
    client.admin.command('ping')  # Test the connection
    logging.info("MongoDB connection successful!")

    db = client[DATABASE_NAME]

    # List of collections to fetch
    collections_to_fetch = ["users", "movies", "comments"]

    for collection_name in collections_to_fetch:
        logging.info(f"Fetching data from collection: {collection_name}...")

        # Ensure the collection exists
        if collection_name not in db.list_collection_names():
            logging.warning(f"Collection '{collection_name}' does not exist. Skipping.")
            continue

        # Fetch data from the collection
        collection = db[collection_name]
        data = list(collection.find())

        if not data:
            logging.warning(f"Collection '{collection_name}' is empty. Skipping.")
            continue

        # Save data to a JSON file
        file_path = os.path.join(DATA_DIR, f"{collection_name}.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2, default=serialize)
        logging.info(f"Data saved to {file_path}.")

    # Create a flag file to signal completion
    with open(FLAG_FILE, "w") as f:
        f.write("MONGODB_FETCH_COMPLETE")
    logging.info(f"Flag file created: {FLAG_FILE}")

except Exception as e:
    logging.error(f"An error occurred: {e}")
    exit(1)
