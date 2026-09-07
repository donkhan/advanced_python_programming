from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0"
)

db = client["college"]
students = db["students"]

students.insert_many([
    {
        "name": "Rahul",
        "age": 22,
        "email": "rahul@example.com"
    },
    {
        "name": "Anita",
        "age": 19,
        "email": "anita@example.com"
    },
    {
        "name": "Vikram",
        "age": 25,
        "email": "vikram@example.com"
    },
    {
        "name": "Priya",
        "age": 28,
        "email": "priya@example.com"
    },
    {
        "name": "Arjun",
        "age": 32,
        "email": "arjun@example.com"
    }
])

print("Documents inserted successfully")