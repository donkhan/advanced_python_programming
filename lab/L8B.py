import requests

#country = input("Enter country code: ")
#year = input("Enter year: ")

country = "IND"
year = "2020"

url = f"https://api.worldbank.org/v2/country/{country}/indicator/SP.POP.TOTL"
url = f"http://127.0.0.1:5000/v2/country/{country}/indicator/SP.POP.TOTL"


params = {
    "date": year,
    "format": "json"
}

response = requests.get(url, params=params)
print(response.json)
if response.status_code == 200:
    data = response.json()
    print(data)
    if len(data) > 1 and data[1]:
        record = data[1][0]

        print("\nPopulation Information")
        print("----------------------")
        print("Country:", record["country"]["value"])
        print("Year:", record["date"])
        print("Population:", record["value"])

    else:
        print("No population data found.")

else:
    print("Unable to retrieve data.")