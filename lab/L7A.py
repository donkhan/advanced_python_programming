import requests
from bs4 import BeautifulSoup

url = "https://edition.cnn.com"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("span")
count = 0
for headline in headlines:
    text = headline.get_text(strip=True)
    if len(text) > 40:
        print(text)
        count += 1
    if count == 100:
        break