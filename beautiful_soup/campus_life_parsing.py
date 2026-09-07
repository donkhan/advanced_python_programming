from bs4 import BeautifulSoup

with open("html/campus_life.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")


def is_rainy_walk(tag):
    return tag.name == "article" and tag.find("span",class_="location").text == "University Garden"

rw = soup.find(is_rainy_walk)
print(rw.find_all("span", class_="name"))