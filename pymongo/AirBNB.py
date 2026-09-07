from pymongo import MongoClient

client = MongoClient("mongodb+srv://pu:pp@cluster0.vdvk1xm.mongodb.net/?appName=Cluster0")
db = client["sample_airbnb"]
listings = db.get_collection("listingsAndReviews")

l = listings.find({}, {"name": 1, "_id" : 0 }).limit(5)

l = listings.find({"property_type": "Apartment"})
l = listings.find({"accommodates" : { "$gt" : 2}})
l = listings.find({"number_of_reviews" : { "$gt" : 100}})
l = listings.find({
        "$and":[
            {"property_type": "Apartment"},
            {"accommodates" : { "$gte" : 4}}
        ]
    }
)
# OR
l = listings.find({
    "property_type": "Apartment",
    "accommodates": {"$gte": 4}
})

#OR
l = listings.find({
    "price": {
        "$gt": 100,
        "$lt": 300
    }
})

l = listings.find({
     "property_type": "Apartment",
     "address.country": "Portugal"

})

for r in l:
    print(r)


# 1. Display 5 Airbnb listings.
# 2. Display the names of all listings.
# 3. Find all listings whose property_type is "Apartment".
# 4. Find all listings that accommodate more than 6 people.
# 5. Find all listings having more than 100 reviews.
# 6. Find all "Apartment" listings that accommodate at least 4 people.
# 7. Find all listings where the price is greater than 100 and less than 300.
# 8. Find all listings in "Portugal" country whose property type is "Apartment"
#Find all listings where number_of_reviews is 0.
#Find all listings where the field reviews exists.
#Find all listings that have "Wifi" in their amenities array.
#Find all listings that have BOTH "Wifi" and "Kitchen" in their amenities array.
#Find all listings whose address.country is "United States".
#Find all listings whose room_type is "Entire home/apt" and whose price is less than 200.
#Display only the following information for every listing:
 #   name
 #   property_type
 #   room_type
 #   price
#Find one particular listing using its _id and change its name.
#Increase the price of all listings in "Entire home/apt" by 10.
#Add a new field called category with value "Premium" to all listings whose price is greater than 500.
#Delete one listing using its _id.
#Delete all listings whose number of reviews is 0.

