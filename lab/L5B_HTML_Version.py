import requests
from bs4 import BeautifulSoup

with open("L5B.html","r") as fd:
    content = fd.read()

soup = BeautifulSoup(content, "html.parser")
headlines = soup.select("span.titleline a")
print("{:<5} {:<70} {}".format("No.", "Headline", "Link"))
print("-" * 150)

for i, item in enumerate(headlines, start=1):
    title = item.get_text(strip=True)
    link = item.get("href")
    print("{:<5} {:<70} {}".format(i, title[:68], link))