import pandas as pd

chocolates = pd.read_csv("/tmp/flavors_of_cocoa.csv")
chocolates.rename(columns={"Company Location": "Location"}, inplace=True)
chocolates["Cocoa Percent"] = chocolates["Cocoa Percent"].str.rstrip("%").astype(float)


print(chocolates.groupby("Location").count())
print(chocolates.groupby("Location").value_counts())


#print(chocolates.groupby("Location").count()["Company"])
#print(chocolates.groupby("Location").size())

#11 Find the minimum and maximum Cocoa Percent in the dataset.
#print(chocolates.agg({
#    "Cocoa Percent" : ["min","max"]
#}))

#17. Find the average Rating of chocolates manufactured in France.
#print(chocolates[
#    chocolates['Location'] == 'France'
#]['Rating'].mean())

#22. Sort the DataFrame by  Location (ascending) and Rating (descending).
#print(chocolates.sort_values(by=["Location", "Rating"], ascending=[True,False]))

#28. Find the Location having the highest average Rating.
#print(chocolates.groupby("Location").agg({
#    "Rating": "mean"
#}).nlargest(1, "Rating"))

#33. Display the chocolates manufactured in the Location having the maximum number of chocolates.
#location = chocolates.groupby("Location").agg({
#    "Company": "count"
#}).nlargest(1, "Company")

#print(chocolates[
#    chocolates["Location"].isin(location.index)
#])


#38. Display all chocolates whose Rating is equal to the highest Rating in their Location.
#print(chocolates[
#    chocolates['Rating'] == chocolates.groupby("Location")['Rating'].transform("max")
#])

#43. For each Location, display: Average Rating,Minimum Cocoa Percent,Maximum Cocoa Percent,Number of Company.
#print(chocolates.groupby("Location").agg({
#    "Rating": "mean",
#    "Cocoa Percent": ["min", "max"],
#    "Company": "nunique"
#}))

#46. Display the top 5 highest-rated chocolates from each Location.
#print(chocolates.sort_values(by=["Location", "Rating"], ascending=[True, False]).groupby("Location").head(5))

#54. Display the top 2 chocolates from each Location after sorting by Company name.
#print(chocolates.sort_values(by=["Company","Rating"],ascending=[True,False]).groupby("Location").head(2))

#print(chocolates.sort_values(by=["Company","Rating"],ascending=[True,False]).groupby("Location").nth(2))

#1A Display chocolates whose rating is better than avg rating of their location
#location_rating = chocolates.groupby("Location")["Rating"].transform("mean")
#print(chocolates[
#    chocolates['Rating'] > location_rating
#])

#2A Display chocolates whose Rating is greater than the average Rating of their Company but whose Cocoa Percentage is
# less than the average Cocoa Percentage of their Company

#avg_rating = chocolates.groupby("Company")["Rating"].transform("mean")
#avg_cocoa = chocolates.groupby("Company")["Cocoa Percent"].transform("mean")

#print(chocolates[
#    (chocolates["Rating"] > avg_rating) &
#    (chocolates["Cocoa Percent"] < avg_cocoa)
#])

#3A Display chocolates whose Rating is greater than the average Rating of their Company
# but whose Company itself has a below-average Rating compared to all Companies.

#company_average = chocolates.groupby("Company")["Rating"].transform("mean")
#avg = (
#    chocolates.groupby("Company")["Rating"]
#              .mean()
#              .mean()
#)

#print(chocolates[
#    (chocolates["Rating"] > company_average) &
#    company_average < avg
#])

#53. Display the second chocolate alphabetically (Company) from each Location.
#print(chocolates.sort_values(by=["Location","Company"]).groupby("Location").nth(1))


# understanding loc and iloc
#print(chocolates.loc[2])
# deprecated
#print(chocolates.loc[2][1:4])

#print(chocolates.iloc[32])
#print(chocolates.iloc[32][3:4])


# Last Row
#print(chocolates.iloc[-1])

# First 5 Rows
#print(chocolates.iloc[0:5])

# Every 3rd Row
#print(chocolates.iloc[0:len(chocolates):3])
#print(chocolates.iloc[0:0:3])

# Last column of all rows
#print(chocolates.iloc[:, -1])

#Display all rows except every fifth row.
#print(chocolates.drop(chocolates.index[4::5]))

#Display the first and last rows together.
#print(chocolates.drop(chocolates.index[1:-1]))
#Random selection of rows
#print(chocolates.iloc[[0, 2, 10, -1]])

#Display Last 3 columns
#print(chocolates.iloc[:, -3:])

#Display rows 10 to 20 and columns 2 to 5.
#print(chocolates.iloc[10:21, 2:6])

#Display the first and last three rows together.
#print(chocolates.iloc[[0,1,2,-3,-2,-1]])

#Display the first 10 rows but only alternate columns.
#print(chocolates.iloc[0:10,::2])

#Display all rows but every alternate column in reverse order.
#print(chocolates.iloc[:, -1::-2])

#Display the last 10 rows in reverse order.
#print(chocolates.iloc[-1:-11:-1])

#Display the entire DataFrame with both rows and columns reversed.
#print(chocolates.iloc[::-1,::-1])

#print(len(chocolates))
#print(chocolates['Company'].count())


