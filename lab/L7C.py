import requests
from bs4 import BeautifulSoup

location = input("Enter location: ")
url = f"https://wttr.in/{location}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()
# Display the weather report
print("\n" + "=" * 40)
print("      CURRENT WEATHER REPORT")
print("=" * 40)
print(text)
print("=" * 40)