from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["ai_website_builder"]
collection = db["projects"]
