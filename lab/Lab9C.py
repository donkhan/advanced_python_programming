from pymongo import MongoClient

client = MongoClient("<MongoDB Atlas connection string>")


db = client["college"]
students = db["students"]

# Update the email address of Rahul
students.update_one(
    {"name": "Rahul"},
    {"$set": {"email": "rahul_new@example.com"}}
)

# Display the updated document
student = students.find_one({"name": "Rahul"})

print(student)