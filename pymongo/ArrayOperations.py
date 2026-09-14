from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
db = client["db-inv"]
inventory = db["inventory"]


results = inventory.find()
for r in results:
    print(r)

# All Operator

# The following operation uses the $all operator to query the inventory collection for documents
# where the value of the tags field is an array whose elements include appliance, school, and book

results = inventory.find({"tags": {"$all": ["appliance", "school", "book"]}})

# Elem Match Operator
# The value of the qty field is an array whose elements match the $elemMatch criteria:
results = inventory.find( {
                     "qty": { "$all": [
                                    { "$elemMatch" : { "size": "M", "num": { "$gt": 50} } },
                                    { "$elemMatch" : { "num" : 100, "color": "green" } }
                                  ] }
                   } )

# Non Array Field
results = inventory.find( { "qty.num": { "$all": [ 50 ] } } )


for r in results:
    print(r)

# Any Operator



