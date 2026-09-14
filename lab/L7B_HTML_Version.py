from bs4 import BeautifulSoup


with open("L7B.html","r") as fd:
    content = fd.read()


soup = BeautifulSoup(content, "html.parser")
headlines = soup.find_all("span")
count = 0
for headline in headlines:
    text = headline.get_text(strip=True)
    if len(text) > 40:
        print(text)
        count += 1
    if count == 100:
        break