from bs4 import BeautifulSoup


with open("L7C.html","r") as fd:
    content = fd.read()

soup = BeautifulSoup(content, "html.parser")
text = soup.get_text()
# Display the weather report
print("\n" + "=" * 40)
print("      CURRENT WEATHER REPORT")
print("=" * 40)
print(text)
print("=" * 40)