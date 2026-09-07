import pandas as pd
chocolates = pd.DataFrame({
    "Company": ["A", "B", "C", "D", "E"],
    "Location": ["France", "France", "France", "Canada", "Canada"],
    "Rating": [4.0, 3.5, 3.8, 4.2, 3.8],
    "Cocoa Percent": [70, 75, 80, 70, 75]
})

print(chocolates)

#avg = chocolates.groupby("Location")["Rating"].transform("mean")
#print(chocolates[chocolates['Rating'] > avg])

avg = chocolates.groupby("Location")["Rating"].transform("mean")
#print(chocolates[chocolates['Rating'] < avg][['Company', 'Location', 'Rating', 'Cocoa Percent']])

max_series = chocolates.groupby("Location")["Rating"].transform("max")
#print(chocolates[chocolates['Rating'] == max_series][['Company', 'Location', 'Rating', 'Cocoa Percent']])

#max_series = chocolates.groupby("Location")["Cocoa Percent"].transform("max")
#print(chocolates[chocolates['Cocoa Percent'] == max_series][['Company', 'Location', 'Rating', 'Cocoa Percent']])

#print(chocolates.groupby("Location")['Rating'].agg(['min', 'max', 'mean', 'count']))

#print(chocolates.groupby("Location").agg(
#    {
#        "Rating" : "mean",
#        "Cocoa Percent" : "mean",
#        "Company" : "count"
#    }
#))


#print(chocolates.groupby("Location").agg(
#    {
#        "Rating": "mean",
#        "Cocoa Percent": ["min", "max"],
#        "Company": "count"
#    }
#))

#print(chocolates.groupby("Location").agg(
#    {
#        "Rating": ["mean", "min", "max"],
#        "Cocoa Percent": "mean",
#        "Company": "count"
#    }
#))

#print(chocolates.groupby("Location").agg(
#    {
#        "Rating": ["mean", "min", "max"],
#        "Cocoa Percent": "mean",
#        "Company": "count"
#    }
#).sort_values(("Rating","mean"),ascending=False))


#print(chocolates.groupby("Location").aggregate(
#    Avg_Rating=pd.NamedAgg(column="Rating", aggfunc='mean'),
#    Avg_CocoaPercent=pd.NamedAgg(column="Cocoa Percent", aggfunc='mean')
#))

#print(chocolates.groupby("Location")['Rating'].agg("mean").sort_values(ascending=False))

#Display the Company, Location, Rating, and Cocoa Percent columns for chocolates whose Rating is equal to the minimum Rating of their Location.
#min_rating = chocolates.groupby("Location")['Rating'].transform("min")
#print( chocolates[
#    chocolates['Rating'] == min_rating
#][['Company', 'Location', 'Rating', 'Cocoa Percent']])

#print(chocolates.groupby("Location").agg({
#    "Rating": ["min", "max"],
#    "Cocoa Percent": ["mean"]
#}).sort_values(("Cocoa Percent","mean"),ascending=False))


#Display all chocolates whose Rating is greater than the average Rating of their Location and
# whose Cocoa Percent is greater than the average Cocoa Percent of their Location.

average_rating = chocolates.groupby("Location")["Rating"].transform("mean")
average_cocoa = chocolates.groupby("Location")["Cocoa Percent"].transform("mean")
output = chocolates[
    (chocolates["Rating"] > average_rating) &
    (chocolates["Cocoa Percent"] > average_cocoa)
]
#print(output)

max_rating = chocolates.groupby("Location")["Rating"].transform("max")
min_cocoa = chocolates.groupby("Location")["Cocoa Percent"].transform("min")


output = chocolates[
    ( chocolates['Rating'] == max_rating) |
    ( chocolates['Cocoa Percent'] == min_cocoa)
]

#print(output)


# Display the top 2 highest-rated chocolates from each Location.
#print(chocolates.sort_values(by=["Location", "Rating"], ascending=[True, False]).groupby("Location").head(2))

#Display the bottom 3 chocolates from each Location based on Rating.
#print(chocolates.sort_values(by=["Location", "Rating"]).groupby("Location").tail(3))

# Display Display the second highest-rated chocolate from each Location.
#print(chocolates.sort_values(by=["Location", "Rating"], ascending=[True, False]).groupby("Location").nth(1))


