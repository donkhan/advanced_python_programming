from pymongo import MongoClient

#client = MongoClient("<MongoDB Atlas connection string>")

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
db = client["college"]
students_collection = db["students"]

student = {
    "roll": 201,
    "name": "Aarav",
    "specialization": "Data Science",
    "semester": 2,
    "cgpa": 8.7,
    "city": "Bangalore",
    "projects": {
        "title": "Petroleum Production Prediction",
        "technology": "Python"
    }
}

students = [
    {
        "roll": 201,
        "name": "Aarav",
        "specialization": "Data Science",
        "semester": 2,
        "cgpa": 8.7,
        "city": "Bangalore"
    },
    {
        "roll": 202,
        "name": "Diya",
        "specialization": "Artificial Intelligence",
        "semester": 2,
        "cgpa": 9.1,
        "city": "Chennai"
    },
    {
        "roll": 203,
        "name": "Rohan",
        "specialization": "Cyber Security",
        "semester": 2,
        "cgpa": 7.8,
        "city": "Hyderabad"
    },
    {
        "roll": 204,
        "name": "Ishita",
        "specialization": "Data Science",
        "semester": 2,
        "cgpa": 9.3,
        "city": "Bangalore"
    },
    {
        "roll": 205,
        "name": "Aditya",
        "specialization": "Cloud Computing",
        "semester": 2,
        "cgpa": 8.2,
        "city": "Mysore"
    },
    {
        "roll": 206,
        "name": "Nisha",
        "specialization": "Artificial Intelligence",
        "semester": 2,
        "cgpa": 8.9,
        "city": "Bangalore"
    },
    {
        "roll": 207,
        "name": "Vikram",
        "specialization": "Cyber Security",
        "semester": 2,
        "cgpa": 7.4,
        "city": "Chennai"
    },
    {
        "roll": 208,
        "_id": 12,
        "name": "Sneha",
        "specialization": "Data Science",
        "semester": 2,
        "cgpa": 9.0,
        "city": "Hyderabad"
    }
]

# students_db.delete_many({})
# result = students_db.insert_one(student)
# print("Document inserted:", result.inserted_id)

# students_db.insert_many(students)
# Find All students
results = students_collection.find()


# counting documents
print(students_collection.count_documents({"specialization" : "Data Science"}))
# select count(*) from students where specialization = "Data Science"

# Display only students whose CGPA is greater than 8.5.
results = students_collection.find(
    {"cgpa":
         {"$gt": 8.5 }
     }
)

# Display all M.Sc. students whose CGPA is between 8.0 and 9.0, inclusive.
results = students_collection.find({
    "$and": [
        {"cgpa": {"$gte": 8}},
        {"cgpa":  {"$lte": 9 }}
    ]
})

results = students_collection.find(
    {
        "cgpa": {
            "$gte": 8,
            "$lte": 9
        }
    }
)

# Find all students whose specialization is "Data Science".
results = students_collection.find({"specialization" : "Data Science"})

# Find all Data Science students whose CGPA is greater than 8.5.
results = students_collection.find({
    "$and": [
        {"specialization" : "Data Science"},
        {"cgpa": {"$gt": 8.5}}
    ]
})

# Update a record
result = students_collection.find_one({"roll": 204})
print(result)
result = students_collection.update_one(
    {"roll": 204},
    {'$set':
         { 'cgpa': 9.5 }
    }
)
print("Modified:", result.modified_count)
result = students_collection.find_one({"roll": 204})
print(result)


students_collection.update_many(
    {
        "specialization": "Cyber Security"
    },
    {
        "$inc": {
            "cgpa": 0.2
        }
    }
)
# All students specializing in Cyber Security should receive a CGPA bonus of 0.2.
results = students_collection.find({"specialization": "Cyber Security"})

# "Cyber Security" is now officially called "Cyber Security and Digital Forensics".
students_collection.update_many(
    {"specialization": "Cyber Security"},
    {"$set": {
        "specialization": "Cyber Security and Digital Forensics"
    }}
)

#All students with CGPA ≥ 9.0 should be marked as "Distinction"
students_collection.update_many(
    {
        "cgpa": {"$gte": 9.0}
    },
    {
        "$set": {
            "grade": "Distinction"
        }
    }
)




results = students_collection.find()
for r in results:
    print(r)


try:
    database = client["sample_fruit"]
    collection = database["fruits"]

    #collection.insert_many([
     #   { "_id": 1, "name": "apples", "qty": 5, "rating": 3, "color": "red", "type": ["fuji", "honeycrisp"] },
      #  { "_id": 2, "name": "bananas", "qty": 7, "rating": 4, "color": "yellow", "type": ["cavendish"] },
      #  { "_id": 3, "name": "oranges", "qty": 6, "rating": 2, "type": ["naval", "mandarin"] },
      #  { "_id": 4, "name": "pineapple", "qty": 3, "rating": 5, "color": "yellow" },
    # ])

    results = collection.find({"color": "yellow"})
    results = collection.find({"rating": {"$gt": 2}})
    results = collection.find({
        "$or": [
            {"qty": {"$gt": 5}},
            {"color": "yellow"}
        ]
    })

    # Array Operator
    results = collection.find({
        "type": {"$size": 2}
    })

    # Element Operator
    results = collection.find({"color": {"$exists": False}})

    # Evaluation Operators
    results = collection.find({"name": {"$regex": "p{2,}"}})

    client.close()

except Exception as e:
    raise Exception("Error: ", e)

