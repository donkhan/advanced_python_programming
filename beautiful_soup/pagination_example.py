import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-48.html"

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("\nPAGE:", url)

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        print(book.find("h3").find("a").get("title"))

    next_link = soup.find("li", class_="next")

    if next_link is None:
        print("Stopped as next_link is not provided")
        break

    url = "https://books.toscrape.com/catalogue/" + next_link.find("a").get("href")