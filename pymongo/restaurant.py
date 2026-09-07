from pymongo import MongoClient

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
db = client["restaurant"]
restaurants = db.get_collection("restaurants")


# Insert One
restaurants.restaurants.insert_one({"name" : "Mongo's Burgers"})

# Insert Many
document_list = [
   { "name" : "Mongo's Burgers" },
   { "name" : "Mongo's Pizza" }
]

restaurants.restaurants.insert_many(document_list)

results = restaurants.find()
for r in results:
    print(r)




