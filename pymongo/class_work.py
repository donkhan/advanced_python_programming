from datetime import datetime

from pymongo import MongoClient

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
db = client["sample_analytics"]
customers = db["customers"]


# 1. Find All
results = customers.find()

# 2. Rahul
#print(db.customers.find_one())

# 3. Unaiza
for i in db.customers.find({'username':'keithbuck'}):
    print(i)


#4.Ranjan
results=db.customers.find(
    {'username':'keithbuck'},
    {'name':1,'email':1,'_id':0}
)

for i in results:
    print(i)
    #pass

