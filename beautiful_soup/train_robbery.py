from bs4 import BeautifulSoup

with open("html/train_robbery.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
#print(soup)


# Using the fixed HTML, how would you get the title of the HTML document?
#print(soup.find("title").text)

# How would you get the text inside the <h1> tag?
#print(soup.find("h1").text)

# How would you get all six <div class="scene"> elements?
#print(soup.find_all("div",class_="scene"))

# How would you print the heading of every scene, one per line?
scenes = soup.find_all("div", class_="scene")
for scene in scenes:
    #print(scene.find("h2").text)
    pass

# How would you find the scene whose scene as 4:
# get data-location
for scene in scenes:
    if scene.get("data-scene") == "2":
        #print(scene.find("h2").text)
        pass

# How would you get the first character appearing in the entire film?
# print(soup.find("div").find("div").find("span").text)
# print(soup.find("div", class_="character").find("span", class_="name").text)

# How would you get all character names from the entire film, without printing the surrounding <div> or <span> tags?

characters = soup.find_all("div", class_="characters")
for character in characters:
    s = character.find_all("span")
    for e in s:
        # print(e.text)
        pass

# Print all the character names appearing in Scene 3 only.
for scene in scenes:
    if scene.get("data-scene") == "3":
        s = character.find_all("span",class_="name")
        for e in s:
            #print(e.text)
            pass

# Find the <div class="character"> representing Detective, but only within Scene 3, without a loop.
#print(soup.find("div", class_="scene", attrs={"data-scene": "3"}).find("div",class_="character"))

# Still using Scene 3, find the <div class="character"> whose data-role is "villain".
#print(soup.find("div", class_="scene", attrs={"data-scene": "3"}).
#      find("div",class_="character", attrs={"data-role":"villain"}))

# Now suppose I want the name of the villain in Scene 3, not the whole <div>.
#print(soup.find("div", class_="scene", attrs={"data-scene": "3"}).
#     find("div",class_="character", attrs={"data-role":"villain"}).find("span").text)

# Q13  gettint parent

villain = soup.find(
    "div",
    class_="scene",
    attrs={"data-scene": "3"}
).find(
    "div",
    class_="character",
    attrs={"data-role": "villain"}
)

# print(villain.parent.parent.get('data-scene'))

# Q15 . All children
scene3 = soup.find("div", class_="scene", attrs={"data-scene": "3"})
#print(scene3.children)

# !7 Using scene3, how would you print the text of every <p> element anywhere inside Scene 3,
# regardless of how deeply nested it is?
descendants = scene3.descendants
for descendant in descendants:
    if descendant.name == 'p':
        # print(descendant.text)
        pass

# Get Scene 4 from Scene 3
scene4 = scene3.find_next_sibling("div", class_="scene")
# print(scene4)

# Get Scene 3 from 4
# print(scene4.find_previous_sibling("div", class_="scene"))

# Q20 For each scene, determine whether it contains a character whose data-role is "hero" —
# and print that scene's heading.
for scene in scenes:
    characters = scene.find_all("div", class_="character")
    for character in characters:
        if character.get("data-role") == "hero":
            # print(scene.find("h2").text)
            break

# Q21 Can you rewrite the condition so that you don't need the inner for character loop?
for scene in scenes:
    if scene.find("div", class_="character", attrs={"data-role": "hero"}) is not None:
        #print(scene.find("h2").text)
        pass

# Q22 Find all scenes in which both the Detective (hero) AND the Bandit Leader (villain) appear.
for scene in scenes:
    if scene.find("div", class_="character", attrs={"data-role": "hero"}) is not None \
            and scene.find("div", class_="character", attrs={"data-role": "villain"}) is not None :
       #print(scene.find("h2").text)
       pass

# Q23 How many times do the Detective and Bandit Leader appear together?
c = 0
for scene in scenes:
    if scene.find("div", class_="character", attrs={"data-role": "hero"}) is not None \
            and scene.find("div", class_="character", attrs={"data-role": "villain"}) is not None :
        c = c + 1
#print(c)


# Q24 Instead of counting the scenes, print the locations of every scene where the Detective
# and Bandit Leader appear together.
for scene in scenes:
    if scene.find("div", class_="character", attrs={"data-role": "hero"}) is not None \
            and scene.find("div", class_="character", attrs={"data-role": "villain"}) is not None :
        #print(scene.get("data-location"))
        pass


# Q25 From scene3, find the next scene's heading (Scene 4: The Escape) without searching from soup
# and without using the data-scene attribute.
# print(scene3.find_next_sibling("div",attrs={"class":"scene"}).find("h2").text)


# Prepare a list of dictionaries scene by scene
l = []
for scene in scenes:
    d = {}
    d['scene'] = scene.get("data-scene")
    d['heading'] = scene.find("h2").text
    d['location'] = scene.get('data-location')
    cs = scene.find_all("div", class_="character")
    cl = ''
    for c in cs:
        cl = cl + "," + c.find("span").text
    d['characters'] = cl[1:]
    l.append(d)
# print(l)


# Q26 How would you find the <div class="action"> inside Scene 3 and then print all the actions in that scene?
scene3 = soup.find("div", class_="scene", attrs={"data-scene": "3"})
action = scene3.find("div", class_="action")
for p in action.find_all("p"):
    #print(p.text)
    pass

# 27 How would you move from action upward to the <div class="scene"> that contains it?
# print(action.parent)

# 28 How would you get the <p> element containing the text "The detective secretly observes the robbery.
# " without looping through the paragraphs?
x = action.find("p", string="The detective secretly observes the robbery.")
# print(x)


def contains_detective(text):
    return "detective" in text


# Q29 Now we don't know the complete sentence. We only know that the paragraph contains the word "detective".
x = action.find("p", string=contains_detective)
# print(x.text)


def is_detective_scene(tag):
    if tag.name == "div" and tag.get("class") == ["scene"]:
        return tag.find(
            "p",
            string=lambda text: text and "detective" in text.lower()
        ) is not None
    return False


# Q30 Find the first scene containing an action paragraph whose text contains the word "detective",
scene = soup.find(is_detective_scene)
#print(scene.find("h2").text)


# Q31 find the source line of scene 3
scene = soup.find("div", class_="scene", attrs={"data-scene": "3"})
# print(scene.sourceline)


# Q32 Using the given HTML, write BeautifulSoup code to determine whether the villain character
# element in Scene 3 is equal to the villain character element in Scene 5.
c1 = soup.find("div", class_="scene", attrs={"data-scene": "3"}).find("div",attrs={"data-role":"villain"})
c2 = soup.find("div", class_="scene", attrs={"data-scene": "5"}).find("div",attrs={"data-role":"villain"})
# print(c1 == c2)
# print(c1 is c1)

c2.find("span", class_="name").string = "Bandit Queen"
with open("modified.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

