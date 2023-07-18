from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")


db = client.DJ


uc = db.User

# uc.insert_one({"un":"python","age":20})