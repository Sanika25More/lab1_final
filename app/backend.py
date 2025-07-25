from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

item_name = input("Enter Item Name: ")
item_description = input("Enter Item Description: ")


todo = {
    "name": item_name,
    "description": item_description
}
collection.insert_one(todo)

print("✅ To-Do item saved to MongoDB successfully!")
