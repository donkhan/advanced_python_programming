from bs4 import BeautifulSoup

with open("html/courses.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")


# You want to find the course <div> that has 4 credits.
def is_4credit_course(tag):
    return tag.name == "div" and tag.get("class") == ["course"] and tag.find("span").text == "Credits: 4"


# print(soup.find(is_4credit_course))


# Find the course <div> for Computer Networks without explicitly iterating.
def is_computer_networks(tag):
    return tag.name == "div" and tag.get("class") == ["course"] and tag.find("h2").text == "Computer Networks"


print(soup.find(is_computer_networks))


