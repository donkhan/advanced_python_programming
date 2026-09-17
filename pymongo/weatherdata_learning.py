from datetime import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_weatherdata"]

# Listing the collection
# print(db.list_collection_names())

weather_data = db["data"]

# print(weather_data.find_one({}))

# 1 Find all documents where the air temperature is greater than 30°C.
results = weather_data.find({
    "airTemperature.value": {
        "$gt": 30
    }
}
)

# 2 Find all documents where the air temperature is between 20°C and 30°C, inclusive.
results = weather_data.find({
    "airTemperature.value": {
            "$gte": 20,
            "$lte": 30
    }
}
)

# 3 Find all documents where:
# airTemperature.value is below 0°C
# AND pressure.value is greater than 1000 hPa
results = weather_data.find({
    "$and": [
        {
            "airTemperature.value": {
                "$lt": 0
            },
            "pressure.value": {
                "$gt": 1000
            }
        }
    ]
})

"OR"

results = weather_data.find({
    "airTemperature.value": {"$lt": 0},
    "pressure.value": {"$gt": 1000}
})


# 4 Find all documents where wind speed is greater than 10.
results = weather_data.find({
    "wind.speed.rate": {"$gt": 10}
})

# 5 Find all documents where the pressure is less than or equal to 1000 hPa.
results = weather_data.find({
    "pressure.value": {"$lte": 1000}
})

for r in results:
    #print(r)
    pass


# 6 Update one document where callLetters is "VCSZ" and set its elevation to 500.
updated_result = weather_data.update_one({
    "callLetters": "VCSZ"
},
{
    # won't work without set operator
    "$set": {
        "elevation": 500
    }
}
)

# 7 Find one document where callLetters is "VCSZ" and change dataSource to "5".
updated_result = weather_data.update_one({
    "callLetters": "VCSZ"
},
{
    "$set": {
        "dataSource": 5
    }
}
)

# 8 Using update_one(), find the document with callLetters: "VCSZ" and increase its elevation by 100.
updated_result = weather_data.update_one({
    "callLetters": "VCSZ"
},
{
    "$inc": {
        "elevation": 100
    }
}
)

# 9 Using update_one(), find the document with callLetters: "VCSZ" and remove the elevation field.
updated_result = weather_data.update_one({
    "callLetters": "VCSZ"
},
{
    "$unset": {"elevation" :""}

}
)



# 10 find all documents where dataSource is "4" and change their dataSource to "5".
updated_result = weather_data.update_many({
    "dataSource": "5"
},
{
    "$set": {
        "dataSource": "4"
    }
}
)

# 11 Find all documents where airTemperature.value is below 0, and set their airTemperature.quality to "9".
updated_result = weather_data.update_many({
    "airTemperature.value": {
        "$lt": 0
    }
},
{
    "$set": {
        "airTemperature.quality": 9
    }
}
)

# 12 Find all documents where pressure.value is greater than 1020, and increase their pressure.value by 5.
updated_result = weather_data.update_many({
    "pressure.value": {
        "$gt": 1020
    }
},
{
    "$inc": {
        "pressure.value": 5
    }
}
)

# 13 Find all documents where wind.speed.rate is greater than 20, and set wind.speed.quality to "1".
updated_result = weather_data.update_many({
    "wind.speed.rate": {
        "$gt": 20
    }
},
{
    "$set": {
        "wind.speed.quality": "1"
    }
}
)

# 14 Find one document where callLetters is "VCSZ" and change its elevation to 1000.
updated_result = weather_data.update_one({
    "callLetters": "VCSZ"
},
{
    "$set": {
        "elevation": 1000
    }
}
)

# 15 Find all weather documents where the observation timestamp ts is after January 1, 1984.
results = weather_data.find({
    "ts": {
        "$gt": datetime(1984, 1, 1)
    }
})

# 16 Find all documents where ts is between March 1, 1984 and March 10, 1984, inclusive of March 1 but before March 10.
results = weather_data.find({
    "ts": {
        "$gte": datetime(1984, 3, 1),
        "$lt": datetime(1984, 3, 10)
    }
})

# 17 Find all documents where ts is after March 1, 1984 AND airTemperature.value is below 0°C
results = weather_data.find({
    "ts": {
        "$gt": datetime(1984, 3, 1)
    },
    "airTemperature.value":{
        "$lt": 0
    }
})

# 18 Find all documents where  ts is before March 5, 1984  AND pressure.value is greater than 1010
results = weather_data.find({
    "ts": {
        "$lt": datetime(1984, 3, 5)
    },
    "pressure.value":{
        "$gt": 1010
    }
})

weather_data.create_index({
    "position": "2dsphere"
})

# 19 Find all documents whose position is within 10 km of the point:
# longitude = -47.9
# latitude  = 47.6
results = weather_data.find({
    "position": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [-47.9, 47.6]
            },
            "$maxDistance": 10000
        }
    }
})

# Near Bengaluru
results = weather_data.find({
    "position": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [77.5946, 12.9716]
            },
            "$maxDistance": 1000000
        }
    }
})

# default unit is metre.
# 20 Find all weather observations within 50 km of:
results = weather_data.find({
    "position": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [-47.9, 47.6]
            },
            "$maxDistance": 50000
        }
    }
})

# 21 Find all documents whose position lies within a 1-degree radius of:
results = weather_data.find({
    "position": {
        "$geoWithin": {
            "$centerSphere": [
                [-47.9, 47.6],
                1 / 6378.1
            ]
        }
    }
})

# 22 Find all documents within approximately 1 km of [-47.9, 47.6] AND where airTemperature.value is below 0°C.
results = weather_data.find({
    "position": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [-47.9, 47.6]
            },
            "$maxDistance": 1000
        }
    },
    "airTemperature.value": {
        "$lt": 0
    }
})

# 23 Find all documents within approximately 1 km of [-47.9, 47.6] AND ts is after March 1, 1984
results = weather_data.find({
    "position": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [-47.9, 47.6]
            },
            "$maxDistance": 1000
        }
    },
    "ts": {
        "$gt": datetime(1984,1,1)
    }
})

# 24 Find all documents where:
# airTemperature.value is below 0
# pressure.value is greater than 1000
# wind.speed.rate is greater than 10
results = weather_data.find({
    "airTemperature.value": {
        "$lt": 0
    },
    "pressure.value":{
        "$gt": 1000
    },
    "wind.speed.rate":{
        "$gt": 10
    }
})

# 26 Find all documents where airTemperature.value is greater than 20, but display only:
# callLetters
# airTemperature
# ts
results = weather_data.find({
    "airTemperature.value": {
        "$gt": 20
    }
},
{
    "callLetters": 1, "airTemperature" : 1, "_id": 0
})

# 27 Find all documents where pressure.value is greater than 1000 and sort them by pressure in descending order.
results = weather_data.find({
    "pressure.value": {
        "$gt": 1000
    }
},
{
    "callLetters": 1,"_id": -1, "pressure.value": 1
}).sort("pressure.value", -1)

# 28 Find all documents where airTemperature.value is below 0,
# sort by temperature from lowest to highest, and return only the first 5 documents.
results = weather_data.find({
    "airTemperature.value": {
        "$lt": 0
    }
},
{
    "callLetters": 1, "_id": 0, "pressure.value": 1, "airTemperature": 1
}).sort("airTemperature.value", 1).limit(5)


# 29 Find all documents where:
#
# airTemperature.value > 20
# pressure.value > 1010

results = weather_data.find({
    "airTemperature.value": {
        "$gt": 20
    },
    "pressure.value":{
        "$gt": 1010
    }
},
{
    "callLetters": 1, "_id": 0, "pressure.value": 1, "airTemperature.value": 1
}).sort("airTemperature.value", -1)


# 30 Find all documents where:
#
# airTemperature.value is below 0,  wind.speed.rate is greater than 10, ts is after March 1, 1984
# Return only:
# callLetters, ts, # airTemperature.value, wind.speed.rate
# Then:
# Sort by airTemperature.value ascending
# Return only 10 documents

results = weather_data.find({
    "airTemperature.value": {
        "$lt": 0
    },
    "wind.speed.rate":{
        "$gt": 10
    },
    "ts":{
        "$gt": datetime(1984, 3, 1)
    }
},
{
    "callLetters": 1, "_id": 0, "airTemperature.value": 1, "wind.speed.rate": 1, "ts": 1
}).sort("airTemperature.value", 1).limit(10)


# Experiment find_update_one
# Upsert
weather_data.update_one(
    {"callLetters": "XYZ99"},
    {"$set": {"elevation": 750}},
    upsert=True
)
# distinct

results = weather_data.distinct("dataSource")

for r in results:
    print(r)



#print(updated_result.matched_count)
#print(updated_result.modified_count)
