import pandas as pd

sales = pd.read_csv("vgsales.csv")
#1. Display only Name, Platform, Global_Sales
#print(sales[["Name","Platform","Global_Sales"]])





#2. Only Published By Ninetendo
#print(sales[sales["Publisher"] == "Nintendo"])

#3. Display only Name, Global Sales published by Ninetdo

#Display the Name, Genre, and Global_Sales of all games that satisfy both conditions:
#Publisher is Nintendo
#Genre is Sports

#print(sales[ (sales["Publisher"] == "Nintendo") & (sales["Genre"] == "Sports")][["Name","Genre","Global_Sales"]] )

#Display the Name, Genre, and Global_Sales of all games that satisfy both conditions:
#Publisher is Nintendo
#Genre is not Sports

#print(sales[ (sales["Publisher"] == "Nintendo") & (sales["Genre"] != "Sports")][["Name","Genre","Global_Sales"]] )

#Display the top 10 Nintendo games (based on Global_Sales)
#s = sales[ sales["Publisher"] == "Nintendo"]
#s = s.sort_values("Global_Sales",ascending=False)
#s = s.head(10)[["Name","Platform","Global_Sales"]]

#Find the total Global_Sales for each Publisher.
#s = sales.groupby("Publisher")["Global_Sales"].sum()
# Prefer the above
#s = sales.groupby("Publisher").sum()["Global_Sales"]


# Find the total Global_Sales for each Genre, and display the result in descending order of Global_Sales.
# This is using Data series
#print(sales.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False))

# This is using Data Frame
#print(sales.groupby("Genre",as_index=False)["Global_Sales"].sum().sort_values("Global_Sales",ascending=False))

#Find the total Global_Sales for each combination of:
#Publisher #Genre
#Sort the result in descending order of Global_Sales.
s = sales.groupby(["Publisher","Genre"],as_index=False)["Global_Sales"].sum().sort_values("Global_Sales",ascending=False)

#Which publisher has released the highest number of games?
#print(sales.groupby("Publisher", as_index=False).count().sort_values("Name",ascending=False)[["Publisher","Name"]].head(1))





