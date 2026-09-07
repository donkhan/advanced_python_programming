import pandas as pd

chocolates = pd.read_csv("/tmp/flavors_of_cocoa.csv")
chocolates.rename(columns={"Company Location": "Location"}, inplace=True)
chocolates["Cocoa Percent"] = chocolates["Cocoa Percent"].str.rstrip("%").astype(float)



print(chocolates.groupby('Location')['Rating'].mean())
#print(chocolates.groupby('Location').mean("Rating"))



french_chocolates = chocolates[
    ( chocolates['Location'] == 'France' ) &
    ( chocolates['Rating'] > 4)
]

rating_of_french_chocolates = french_chocolates['Rating']

print(rating_of_french_chocolates.mean())



# Find the number of different Companies in the dataset.
#print(chocolates["Company"].nunique())

# Find the minimum and maximum Cocoa Percent in the dataset.
#print(chocolates["Cocoa Percent"].aggregate(["max","min"]))


# Display the Company and Rating columns for chocolates manufactured in France having a Rating greater than or equal to 4.0,
# sorted by Rating in descending order.

o = chocolates[
    (chocolates['Location'] == 'France') &
    (chocolates['Rating'] >= 4.0)
].sort_values(by='Rating',ascending=False)[['Company', 'Rating']]

#print(o)

#Display all chocolates whose Rating is greater than the average Rating of their Location, sorted by:

avg_rating = chocolates.groupby("Location")["Rating"].transform("mean")
o = chocolates[
    chocolates['Rating'] > avg_rating
].sort_values(by=["Location", "Rating"],ascending=[True,False])
#print(o)


#Display the top 2 chocolates from each Location after sorting by: Rating (descending) Company (ascending)
#print(chocolates.sort_values(by=["Rating", "Company"],ascending=[False, True]).groupby("Location").head(2))

#Display the top 10 Locations having the highest average Rating, along with the number of chocolates manufactured in each Location.
group = chocolates.groupby("Location")
agg_result = group.agg({
    "Rating": "mean",
    "Company": "count"
})
sort_results = agg_result.sort_values("Rating",ascending=False).head(10)
sort_results.columns = ["Average Rating", "No of Chocolates"]

#print(sort_results)

group = chocolates.groupby("Location")
agg_result = group.agg({
    "Rating": "mean",
    "Cocoa Percent": "mean",
    "Company": "count"
})

sort_results = agg_result.sort_values("Cocoa Percent",ascending=False).head(3)
sort_results.columns = ["Average Rating", "Average Cocoa Percentage", "No of Chocolates"]

#print(sort_results)


#Display the top 5 Locations satisfying both of the following conditions:
#Average Rating is greater than the overall average Rating.
#Number of chocolates is at least 10.

agg_result = chocolates.groupby("Location").agg({
    "Rating": "mean",
    "Company": "count"
})

overall_average = chocolates['Rating'].mean()
filtered_result = agg_result[
    (agg_result['Rating'] > overall_average) &
    (agg_result['Company'] >= 10)
]

sort_result= filtered_result.sort_values("Rating",ascending=False)
top_10 = sort_result.head(10)

#print(top_10)


#Display the top 3 Locations that satisfy all of the following:
#Average Rating > Overall Average Rating.
#Average Cocoa Percent > Overall Average Cocoa Percent.
#Number of chocolates ≥ 10.

#Output should contain:

#Average Rating
#Average Cocoa Percent
#Number of Chocolates

#Sort by:
#Average Rating (descending)
#Average Cocoa Percent (descending)

overall_average_rating = chocolates['Rating'].mean()
overall_average_cocoa_percent = chocolates['Cocoa Percent'].mean()

agg_result = chocolates.groupby("Location").agg({
    "Rating": "mean",
    "Cocoa Percent": "mean",
    "Company": "count"
})

filtered_result = agg_result[
    (agg_result['Rating'] > overall_average_rating) &
    (agg_result['Cocoa Percent'] > overall_average_cocoa_percent) &
    (agg_result['Company'] > 10)
]

sort_result = filtered_result.sort_values(by=["Rating","Cocoa Percent"],ascending=[False, False])
top_3 = sort_result.head(3)
top_3.columns = ["Average Rating", "Average Cocoa Percentage", "Number of Chocolates"]

#print(top_3)


overall_average_rating = chocolates['Rating'].mean()
agg_result = chocolates.groupby("Location").agg({
    "Rating": ["min", "mean"],
    "Company": "count"
})
filtered_result = agg_result[
    (agg_result[("Rating", "min")] >= 1) &
    (agg_result[("Rating", "mean")] >= overall_average_rating) &
    (agg_result[("Company", "count")] >= 10 )
]
sort_result = filtered_result.sort_values(by=[("Rating", "mean"), ("Company", "count")], ascending=[False, False])
top_5 = sort_result.head(5)
#print(top_5)

overall_average_rating = chocolates['Rating'].mean()
locations = chocolates.groupby("Location").agg({
    "Rating": "mean",
    "Company": "count"
})
filtered_locations = locations[
    ( locations['Rating'] > overall_average_rating ) &
    ( locations["Company"] >= 10 )
]

#print(chocolates[
#    chocolates['Location'].isin(filtered_locations.index)
#].sort_values(by=["Location","Rating","Company"],ascending=[True,False,True])[["Company","Location","Rating","Cocoa Percent"]])

#Q72
locations = chocolates.groupby("Location").agg({
    "Rating": "mean"
}).sort_values("Rating", ascending=False).head(5)
#print(chocolates[
#    chocolates['Location'].isin(locations.index)
#][['Company','Location','Rating','Cocoa Percent']])

#print(chocolates.groupby("Location").agg({
#    "Company": "count"
#}))


