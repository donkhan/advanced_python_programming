from pymongo import MongoClient

#client = MongoClient("<MongoDB Atlas connection string>")

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
client = MongoClient("mongodb://localhost:27017")

db = client["college"]
students = db["students"]

student = {
    "name": "Rahul",
    "age": 22,
    "email": "rahul@example.com"
}

result = students.insert_one(student)

print("Document inserted:", result.inserted_id)