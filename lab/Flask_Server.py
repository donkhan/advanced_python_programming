import random
from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route("/quotes")
def quotes():
    with open("L5A.html", "r", encoding="utf-8") as file:
        html = file.read()
    return Response(html, content_type="text/html")


@app.route("/titles")
def titles():
    with open("L5B.html", "r", encoding="utf-8") as file:
        html = file.read()
    return Response(html, content_type="text/html")


@app.route("/headlines")
def headlines():
    with open("L7A.html", "r", encoding="utf-8") as file:
        html = file.read()
    return Response(html, content_type="text/html")


@app.route("/products")
def products():
    with open("L7B.html", "r", encoding="utf-8") as file:
        html = file.read()
    return Response(html, content_type="text/html")


@app.route("/weather")
def weather():
    with open("L7C.html", "r", encoding="utf-8") as file:
        html = file.read()
    return Response(html, content_type="text/html")


# --------------------------------------------------
# Endpoint 2: Geocoding API
# --------------------------------------------------

@app.route("/weather/v1/search")
def geocode():

    # Get request parameters
    city = request.args.get("name")
    count = request.args.get("count")
    language = request.args.get("language")
    response_format = request.args.get("format")

    # Create response
    result = {
        "results": [
            {
                "id": random.randint(1000000, 9999999),
                "name": city,
                "latitude": round(random.uniform(8, 35), 5),
                "longitude": round(random.uniform(68, 97), 5),
                "elevation": round(random.uniform(0, 1000), 1),
                "feature_code": "PPLA",
                "country_code": "IN",
                "admin1_id": random.randint(1000000, 9999999),
                "admin2_id": random.randint(1000000, 9999999),
                "timezone": "Asia/Kolkata",
                "population": random.randint(100000, 10000000),
                "country_id": random.randint(1000000, 9999999),
                "country": "India",
                "admin1": "Karnataka",
                "admin2": "Bengaluru Urban"
            }
        ],
        "generationtime_ms": round(random.uniform(0.1, 1.0), 8)
    }

    return jsonify(result)


@app.route("/v2/country/<country>/indicator/SP.POP.TOTL")
def population(country):

    year = request.args.get("date")

    result = [
        {
            "page": 1,
            "pages": 1,
            "per_page": 50,
            "total": 1,
            "sourceid": "2",
            "lastupdated": "2026-07-13"
        },
        [
            {
                "indicator": {
                    "id": "SP.POP.TOTL",
                    "value": "Population, total"
                },
                "country": {
                    "id": "IN",
                    "value": "India"
                },
                "countryiso3code": country,
                "date": str(year),
                "value": random.randint(100000000, 1500000000),
                "unit": "",
                "obs_status": "",
                "decimal": 0
            }
        ]
    ]

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)