import requests
from bs4 import BeautifulSoup

with open("L5A.html","r") as fd:
    content = fd.read()

soup = BeautifulSoup(content, "html.parser")
quotes = soup.find_all("div", class_="quote")

print("{:<5} {:<70} {:<20}".format("No.", "Quote", "Author"))
print("-" * 100)

for i, quote in enumerate(quotes, start=1):
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    print("{:<5} {:<70} {:<20}".format(i, text[:68], author))