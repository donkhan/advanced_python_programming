import requests

city = input("Enter city name: ")

# Step 1: Find latitude and longitude of the city
geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

geocode_params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

response = requests.get(geocode_url, params=geocode_params)

if response.status_code == 200:
    location_data = response.json()

    if "results" in location_data:
        location = location_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        print("\nLocation:", location["name"])
        print("Country:", location["country"])

        # Step 2: Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "precipitation,"
                "wind_speed_10m"
            )
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params
        )

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            current = weather_data["current"]

            print("\nCurrent Weather")
            print("----------------")
            print("Temperature:", current["temperature_2m"], "°C")
            print("Feels Like:", current["apparent_temperature"], "°C")
            print("Humidity:", current["relative_humidity_2m"], "%")
            print("Precipitation:", current["precipitation"], "mm")
            print("Wind Speed:", current["wind_speed_10m"], "km/h")

        else:
            print("Unable to retrieve weather data.")

    else:
        print("City not found.")

else:
    print("Unable to find the city.")