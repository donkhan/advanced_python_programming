from datetime import datetime

from pymongo import MongoClient

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
db = client["sample_analytics"]
customers = db["customers"]
transactions = db["transactions"]

# 23 Find all documents in transactions where the transactions array contains a transaction satisfying both:
# transaction_code = "buy"
# amount > 9000
results = transactions.find({
    "transactions":{
        "$elemMatch": {
            "transaction_code":"buy",
            "amount" : {
                "$gt" : 9000
            }
        }
    }
})

for transaction in results:
    print(transaction)
exit(1)

# 22 Find customers whose accounts array contains:
# at least one account greater than 800000
# and at least one account less than 100000

results = customers.find({
    "$and":[
        {"accounts": {
            "$gt": 800000
        }},
        {"accounts": {
            "$lt": 100000
        }}
    ]
})



# 21 Find all customers whose accounts array contains at least one value greater than 800000.
results = customers.find({
    "accounts": {
        "$gt": 800000
    }
})




# 20 Find customers whose username is not either "keithbuck" or "davidsonomar".
results = customers.find({
    "username": {
        "$nin" : ["keithbuck", "davidsonomar"]
    }
})




# 1. Find All
customers = customers.find()
for result in customers:
    print(result)
# 2. Find One
# print(customers.find_one())


# 3. User name is keithbuck
results = customers.find(
    {
        "username" : "keithbuck"
    }
)

# 4. Username is keithbuck but project only name and email
results = customers.find(
    {
        "username" : "keithbuck"
    }, {
        "name": 1, "email": 1, "_id": 0
    }
)

# 5. Find all customers whose birthdate is after January 1, 1990.
results = customers.find(
    {
        "birthdate" :{
            "$gt": datetime(1990,1,1)
        }
    }
)

# 6. Born before Jan, 1 ,1970
results = customers.find(
    {
        "birthdate" :{
            "$lt": datetime(1970,1,1)
        }
    }
)

# 7. Find all customers whose birthdate is January 1, 1970 or later.
results = customers.find( { "birthdate" :{ "$gte": datetime(1970,1,1) } } )


# 8 birthdate is after January 1, 1980 and birthdate is before January 1, 1990
results = customers.find(
    {
        "$and": [
            {
                "birthdate": {
                    "$gte": datetime(1980, 1, 1)
                }
            }, {
                "birthdate": {
                    "$lt": datetime(1990, 1, 1)
                }
            }
        ]
    }
)

# 9 user name is keithbuck or davidsonomar
results = customers.find({
    "$or":[
        {
            "username" : "keithbuck"
        },
        {
            "username" : "davidsonomar"
        }
    ]
})

# 10 in operator
results = customers.find({
    "username":{
        "$in":["keithbuck","davidsonomar"]
    }
})

# 11 Find all customers whose username is neither "keithbuck" nor "davidsonomar".
results = customers.find({
    "username":{
        "$not":{
            "$in":["keithbuck","davidsonomar"]
        }
    }
})


# nin operator
results = customers.find({
    "username":{
        "$nin":["keithbuck","davidsonomar"]
    }
})

# 12 Equivalent to any operator
results = customers.find({
    "accounts" : 857689
})


# 13 Now find customers whose accounts array contains either:
# 857689
# 616016

results = customers.find({
    "accounts":{
            "$in":[857689,616016]
    }
})

# 14 All query
results = customers.find({
    "accounts":{
            "$all":[857689,616016]
    }
})


# 14 Find customers who have exactly 4 account numbers in their accounts array.
results = customers.find({
    "accounts":{
            "$size":4
    }
})

# 15 Find an  active customer
results = customers.find({
    "active": True
})

# 16 Find all customers where the email field exists.
results = customers.find({
    "username": {
        "$exists" : True
    }
})

# 17 Find all customers whose username is not "keithbuck".
results = customers.find({
    "not":{
        "username": {
            "ne": "keithbuck"
        }
    }
})

# 19 Find customers whose birthdate is NOT before January 1, 1980.
results = customers.find({
    "birthdate":{
        "$not": {
            "lte": datetime(1980,1,1)
        }
    }
})


for r in results:
    print(r)