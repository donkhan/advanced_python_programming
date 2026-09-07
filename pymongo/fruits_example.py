from pymongo import MongoClient

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
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

for r in results:
    print(r)
client.close()
