import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
url = "http://127.0.0.1:5000/quotes"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

print("{:<5} {:<70} {:<20}".format("No.", "Quote", "Author"))
print("-" * 100)

for i, quote in enumerate(quotes, start=1):
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    print("{:<5} {:<70} {:<20}".format(i, text[:68], author))