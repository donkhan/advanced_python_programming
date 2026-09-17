from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_restaurants"]
# print(db.list_collection_names())
restaurants = db["restaurants"]
# print(restaurants.count_documents({}))

# $match
#    ↓
# $unwind
#    ↓
# $group
#    ↓
# $project
#    ↓
# $sort
#    ↓
# $limit

# 1 Basic Aggregation
result = restaurants.aggregate([
    {
        "$group": {
            "_id": "$borough",
            "count": {"$sum": 1}
        }
    }
])

for r in result:
    print(r)


# 2. Unwind
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    }
])


# 3 Find the average score for each borough.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$borough",
            "av": {"$avg": "$grades.score"}
        }
    }
])


# 4 Find the average score for each borough and sort the boroughs from highest average score to lowest.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$borough",
            "av": {"$avg": "$grades.score"}
        }
    },
    {
        "$sort": {"av": -1}
    }
])

# 4 find the number of restaurants for each cuisine,
# but only for restaurants in Brooklyn.
result = restaurants.aggregate([
    {
        "$match": {
            'borough': 'Brooklyn'
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "count": {"$sum": 1}
        }
    }
])

# 5 Find the highest grade score for each borough.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$borough",
            "max_score": {"$max": "$grades.score"}
        }
    }
])

# 6 Lowest grade score for each borough
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$borough",
            "max_score": {"$min": "$grades.score"}
        }
    }
])

# 7 Find the average grade score for each cuisine,
# but consider only restaurants in Manhattan.
result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Manhattan"
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "max_score": {"$min": "$grades.score"}
        }
    }
])


for r in result:
    print(r)

print(restaurants.find_one({}))
