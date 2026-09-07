import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/s?k=laptop"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", attrs={"data-component-type": "s-search-result"})
print("Products found:", len(products))

# Open CSV file
with open("amazon_products.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header row
    writer.writerow(["Product Name", "Price"])

    # Write product details
    for product in products[:5]:

        title = product.find("h2")
        price = product.find("span", class_="a-price-whole")

        product_name = title.get_text(strip=True) if title else "N/A"
        product_price = price.get_text(strip=True) if price else "N/A"

        print("Title :", product_name)
        print("Price : ₹", product_price)
        print("-" * 60)

        writer.writerow([product_name, product_price])

print("\nData saved successfully to amazon_products.csv")