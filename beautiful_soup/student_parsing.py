from bs4 import BeautifulSoup

with open("html/student.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Title of the html
print(soup.find("head").find("title").text)


# What is inside h1
print(soup.find("body").find("h1").text)

# How would you get all three <p> elements?
para_list = soup.find_all("p")
print(para_list)

# Using para_list, how would you print only the text of each paragraph, one paragraph per line?
for para in para_list:
    print(para.text)

# Suppose the HTML has many <p> tags, but you want to get only the first <p> tag.
soup.find("p")


with open("html/student_with_id.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Get p with id as name
print(soup.find("p", id="name"))

# Get p with id as department
print(soup.find("p", id="department"))

# Get p with class as info
print(soup.find_all("p", class_="info"))
for e in soup.find_all("p", class_="info"):
    print(e.text)

# Get all li elements
print(soup.find("ul").find_all("li"))
for e in soup.find("ul").find_all("li"):
    print(e.text)
