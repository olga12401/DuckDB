import os
import json
import datetime
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch MongoDB connection URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "sample_mflix")
DATA_DIR = os.getenv("DATA_DIR", "/data")

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    client.admin.command('ping')  # Test connection
    print("MongoDB connection successful!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

db = client[DATABASE_NAME]

# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Serialize datetime and ObjectId objects
def serialize(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    if isinstance(obj, ObjectId):
        return str(obj)  # Convert ObjectId to a string
    raise TypeError(f"Type {type(obj)} not serializable")

# Fetch and save data from each collection
COLLECTIONS = ["users", "movies", "comments"]

try:
    for collection_name in COLLECTIONS:
        print(f"Fetching data from collection: {collection_name}...")

        if collection_name not in db.list_collection_names():
            print(f"  - Warning: Collection {collection_name} does not exist.")
            continue

        collection = db[collection_name]
        data = list(collection.find())

        if not data:
            print(f"  - No data found in {collection_name}. Skipping file creation.")
            continue

        print(f"  - {len(data)} documents fetched.")

        # Save data to JSON
        file_path = f"{DATA_DIR}/{collection_name}.json"
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2, default=serialize)

        print(f"  - Data saved to {file_path}.")
    
    print("Data fetching process completed successfully!")

except Exception as e:
    print(f"Error processing collections: {e}")
