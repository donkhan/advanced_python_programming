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


print(restaurants.find_one())


# 1 Basic Aggregation
result = restaurants.aggregate([
    {
        "$group": {
            "_id": "$borough",
            "count": {"$sum": 1}
        }
    }
])

exit(1)


# 1a. Find all restaurants in Brooklyn and display only:
#
# restaurant name
# cuisine
# borough
#
# Do not display _id.

result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Brooklyn"
        }
    },
    {
        "$project": {
            "name": 1,
            "cuisine": 1,
            "_id": 0
        }
    }
])

# 1 c For every restaurant, display:
#
# name
# cuisine
# number_of_grades
#
# where number_of_grades is the number of elements in the grades array.

result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$_id",
            "count": {"$sum": 1},
            "name": {"$first": "$name"},
            "cuisine": {"$first": "$cuisine"},
        }
    },
    {
        "$project":{
            "name": 1,
            "cuisine": 1,
            "_id": 0,
            "count": 1
        }
    }
])

# OR

result = restaurants.aggregate([
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "cuisine": 1,
            "total_grades": {"$size": "$grades"}
        }
    }
])


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


# 4 Find the average score for each borough and
# sort the boroughs from highest average score to lowest.
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
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$cuisine",
            "avg_score": {"$avg": "$grades.score"}
        }
    }
])

# 8 Find the number of restaurants for each cuisine in Queens,
# and sort the result by count from highest to lowest.

result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Queens"
        }
    },
    {
        "$group":{
            "_id": "$cuisine",
             "no_of_restaurants": {"$sum": 1}
        }
    },
    {
        "$sort": {"no_of_restaurants": -1}
    }
])

# 9 Find the average grade score for each cuisine in Brooklyn, and
# show the cuisines from the highest average score to the lowest average score.
result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Brooklyn"
        }
    },
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$cuisine",
            "avg_score": {"$avg": "$grades.score"}
        }
    },
    {
        "$sort": {
            "avg_score": -1
        }
    }
])

print(restaurants.find_one())
# 10 Find the number of grades received by each restaurant,
# and sort the restaurants by the number of grades from highest to lowest.

result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group":{
            "_id": "$_id",
            "nr": {"$sum": 1}
        }
    },
    {
        "$sort": {
            "nr": -1
        }
    }
])


# 11 Find the number of restaurants in each borough that serve American cuisine.
# Sort the result by the number of restaurants from highest to lowest
result = restaurants.aggregate([
    {
        "$match": {
            "cuisine": "American"
        }
    },
    {
         "$group": {
                "_id": "$borough",
                "nr": {
                    "$sum" : 1
                }
            }
    },
    {
        "$sort": {
            "nr": -1
        }
    }
])

# 12 Find the average score for each borough, considering only grade records where the grade is "A"
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.grade": "A"
        }
    },
    {
        "$group":{
            "_id": "$borough",
            "avg_score": {
                "$avg" : "$grades.score"
            }
        }
    }
])
# 13 Find the highest score received by each cuisine, considering all restaurants.
# Sort the result from highest score to lowest score.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$cuisine",
            "max_score": {"$max": "$grades.score"}
        }
    },
    {
        "$sort": {
            "max_score": -1
        }
    }
])

# 14 Find the number of restaurants in each borough that have at least one grade with a score greater than 30.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 30
            }
        }
    },
    {
        "$group":{
            "_id": "$borough",
            "nr": {
                "$sum" : 1
            }
        }
    }
])

# Q15. Find the number of restaurants in each borough whose cuisine is either "American" or "Chinese".
result = restaurants.aggregate([
    {
        "$match": {
            "$or": [
                {"cuisine": "American"},
                {"cuisine": "Chinese"}
            ]
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    }
])

# 16 Find the number of restaurants in each borough where the cuisine is NOT "American".
result = restaurants.aggregate([
    {
        "$match": {
            "cuisine": {
                "$not": {
                    "$regex": "American"
                }
            }
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    }
])

result_ne = restaurants.aggregate([
    {
        "$match": {
            "cuisine": {
                "$ne": "American"
            }
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    }
])

# 17 Find the minimum grade score for each borough, but consider only grades with a score greater than 5.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 5
            }
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "min_score": {
                "$min": "$grades.score"
            }
        }
    }
])

# 18 Find the average grade score for each borough, but consider only restaurants whose cuisine is "Italian".
result = restaurants.aggregate([
    {
      "$unwind": "$grades"
    },
    {
        "$match":{
            "cuisine": "Italian"
        }
    },
    {
        "$group":{
            "_id": "$borough",
            "avg_score": {
                "$avg": "$grades.score"
            }
        }
    }
])

# 19 Find the top 5 cuisines with the highest average grade score across all restaurants.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$cuisine",
            "avg_grade_score": {
                "$avg": "$grades.score"
            }
        }
    },
    {
        "$sort": {
            "avg_grade_score": -1
        }
    },
    {
        "$limit": 5
    }
])

# 20 Find the number of restaurants in each borough that have at least one grade with score less than 5.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$lt": 5
            }
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    }
])

# Important Question
# 21 Find the number of distinct restaurants in each borough that have at least one grade with a score less than 5.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$lt": 5
            }
        }
    },
    {
        "$group": {
            "_id": "$_id",
            "borough": {"$first": "$borough"}
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    }
])

# 22 Find the number of restaurants for each cuisine in Manhattan,
# but count only restaurants that have at least one grade with a score greater than 20.
result = restaurants.aggregate([
    {
      "$match": {
          "borough": "Manhattan"
      }
    },
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 20
            }
        }
    },
    {
        "$group": {
            "_id": "$_id",
            "cuisine": {
                "$first": "$cuisine"
            }
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "nr": {
                "$sum": 1
            }
        }
    }
])


# 23 Find the average grade score for each cuisine in Queens, considering only grades with a score greater than 10.
# Then sort the cuisines by average score, highest to lowest.

result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Queens"
        }
    },
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 10
            }
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "avg_score": {
                "$avg": "$grades.score"
            }
        }
    },
    {
        "$sort": {
            "avg_score": -1
        }
    }
])

# 24 Find the number of restaurants in each borough that have received at least one grade of "A".
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.grade": "A"
        }
    },
    {
        "$group": {
            "_id": "$_id",
            "borough": {
                "$first": "$borough"
            }
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    }
])

# 25 Find the number of restaurants for each cuisine that have at least one grade with a score greater than 40
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 4
            }
        }
    },
    {
        "$group": {
            "_id": "$_id",
            "cuisine": {
                "$first": "$cuisine"
            }
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "nr": {
                "$sum": 1
            }
        }
    }
])

# 26 Find the highest grade score for each cuisine in Brooklyn, considering only grades with a score less than 8.
# Sort by highest score, from highest to lowest.
result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Brooklyn"
        }
    },
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$lt": 8
            }
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "max_score": {
                "$max": "$grades.score"
            }
        }
    },
    {
        "$sort": {
            "max_score": -1
        }
    }
])


# 27 Find the minimum grade score for each cuisine in Queens, considering only grades with a score greater than 3.
# Sort by the minimum score from lowest to highest.
result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Queens"
        }
    },
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 3
            }
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "min_score": {
                "$min": "$grades.score"
            }
        }
    },
    {
        "$sort": {
            "min_score": 1
        }
    }
])


# 28 Find the average grade score for each borough, considering only A grades with a score greater than 5.
# Sort by average score from highest to lowest.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "$and":[
                {
                    "grades.score": {
                        "$gt": 5
                    }
                },
                {
                    "grades.grade": "A"
                }
            ]
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "avg_score": {
                "$avg": "$grades.score"
            }
        }
    },
    {
        "$sort": {
            "avg_score": -1
        }
    }
])

# 29 Find the number of restaurants in each borough that have at least one grade with score exactly 10.
# Count each restaurant only once, even if it has multiple grades with score 10.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score" : 10
        }
    },
    {
      "$group": {
          "_id": "$_id",
          "borough": {
              "$first": "$borough"
          }
      }
    },
    {
        "$group": {
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    }
])

# 30 Find the top 3 boroughs with the highest average grade score, considering only A grades.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.grade": "A"
        }
    },
    {
        "$group": {
            "_id": "$borough",
            "avg_score": {
                "$avg": "$grades.score"
            }
        }
    },
    {
        "$sort": {
            "avg_score": -1
        }
    },
    {
        "$limit": 3
    }
])


# 31 Find the three cuisines in Brooklyn having the highest average grade score, considering
# only grades with a score greater than 5. Return the cuisine and average score, sorted from highest to lowest.
result = restaurants.aggregate([
    {
        "$match": {
            "borough": "Brooklyn"
        }
    },
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 5
            }
        }
    },
    {
        "$group": {
            "_id": "$cuisine",
            "average_score": {
                "$avg": "$grades.score"
            }
        }
    },
    {
        "$sort": {
            "average_score": -1
        }
    },
    {
        "$limit": 3
    }
])

# 32 Find the number of restaurants for each borough that have at least one grade with a score greater than 15.
# Sort the boroughs by this count from highest to lowest.
result = restaurants.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$match": {
            "grades.score": {
                "$gt": 15
            }
        }
    },
    {
        "$group": {
            "_id": "$_id",
            "borough": {
                "$first": "$borough"
            }
        }
    },
    {
        "$group":{
            "_id": "$borough",
            "nr": {
                "$sum": 1
            }
        }
    },
    {
        "$sort": {
            "nr": -1
        }
    }
])




# print(restaurants.find_one({}))
