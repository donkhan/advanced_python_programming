import pandas as pd

# What is series
marks = pd.Series([78, 85, 92, 67, 88])
#print(marks)
#print(type(marks))

# What is Data Frame?
students = pd.DataFrame(
    {
        "Name": ["Rahul", "Priya", "Ayesha", "Vikram"],
        "Age": [22, 23, 21, 24],
        "Marks": [78, 85, 92, 67],
    }
)
#print(students)
#print(students.iloc[1])

# Reading data from csv file
cities = pd.read_csv("CityTable.csv")
#print(cities.describe())

# Understanding Data
# head and tail
#print(cities.head(8))
#print(cities.tail(5))
#print(cities.info())

# Write Data into another format
# need this package openpyxl
#cities.to_excel("cities.xlsx", sheet_name="cities", index=False)

#print(type(cities["name"]))
#print(type(cities[["name", "district"]]))
print(cities[["name", "district"]])

#print(cities.iloc[0])
#print(cities.iloc[5])
#print(cities.iloc[2:7])

large_cities = cities[cities["population"] > 1000000]
#print(large_cities)

indian_cities = cities[cities["country_code"] == "IND"]
#print(indian_cities)

karnataka_cities = cities[cities["district"] == "Karnataka"]
#print(karnataka_cities)

#print(cities.sort_values("population"))

largest = cities.sort_values(
    "population",
    ascending=False
)
print(largest.head(1))

cities["population_lakhs"] = cities["population"] / 100000
#print(cities.head())

cities.rename(
    columns={"district": "state"},
    inplace=True
)

#print(cities.head())
#print(cities.isnull().sum())

# Data Analysis
#print(cities.groupby("country_code")["population"].sum())
#print(cities[cities["country_code"] == 'IND'].groupby("state")["population"].sum())

result = cities.groupby(["country_code", "state"])["population"].sum()
#print(result)
# Total population grouped by Country and State
result = (
    cities.groupby(["country_code", "state"])["population"]
          .sum().reset_index()
)
print(result)

result=cities.groupby("country_code")["population"].sum()

#print(result.idxmax())
#print(result.max)
#print(result.nlargest(1))



result = (
    cities.groupby("country_code")["population"]
          .sum()
          .reset_index()
          .sort_values(by="population", ascending=False)
)
#print(result.head(1))

x = cities[cities["country_code"] == 'IND']
result = x.groupby(["country_code", "state"])["population"].sum().reset_index().sort_values(by="population", ascending=False)

#print(result.head(1))