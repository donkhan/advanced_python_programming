from pymongo import MongoClient



client = MongoClient(
    "mongodb+srv://pythonuser:python123@cluster0.xxxxx.mongodb.net/"
)

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
db = client["college"]
students = db["students"]

# Find students whose age is between 20 and 30
results = students.find({
    "age": {
        "$gte": 20,
        "$lte": 30
    }
})

for student in results:
    print(student)