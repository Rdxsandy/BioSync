# database/db.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

print("MongoDB URL:", MONGODB_URL)

client = MongoClient(MONGODB_URL)

try:
    client.admin.command("ping")
    print("MongoDB connected successfully")
except Exception as e:
    print("MongoDB connection failed:", e)

# database
db = client["stockhomelm"]

# test collections
users_collection = db["users"]
activity_collection = db["activities"]
meals_collection = db["meals"]
health_collection = db["health"]


