from bs4 import BeautifulSoup

with open("html/college.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Get Rahul's record
students = soup.find("div", id="students").find_all("div", class_="student")
for e in students:
    if e.find("h2").text == "Rahul":
        print(e.find_all("p")[0].text)


def is_rahul(tag):
    return (tag.name == "div" and
            tag.get("class") == ["student"] and
            tag.find("h2").text == "Rahul")


student = soup.find(is_rahul)
print(student)
