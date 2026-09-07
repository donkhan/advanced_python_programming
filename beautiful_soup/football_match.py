from bs4 import BeautifulSoup

with open("html/football_2026_final.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

#print(soup.find("section",class_="attendance").find("p").text)

# Q1. Find and print the title of the HTML document.
print(soup.find("title").get_text())

# Q2. Find the match <div> and print its data-stage attribute.
match_div=soup.find('div',attrs={'data-stage':True})
print(match_div.get('data-stage'))

# Q3. Find and print the names of both teams.
for e in soup.find_all("div",class_="team"):
    print(e.find("h3").get_text())


# Q4. Find the away team and print its country and score.

# Q5. Find and print the winner of the match.

# Q6. Find all match events and print the complete text of each event.

# Q7. Find all yellow-card events and print the player involved.

# Q8. Find all events involving Argentina and print the event type and player information.

# Q9. Find the event at the 106th minute and print the complete HTML of that event.

# Q10. Find the goal event and print the name of the player who scored.

# Q11. Find the red-card event involving Enzo Fernandez and print its complete text.

# Q12. Find all substitutions made by Spain and print their complete text.

# Q13. Find the events section and navigate to its parent element.
#     Print the id of the parent.

# Q14. Find the yellow-card event and red-card event involving Enzo Fernandez.
#     Compare the two BeautifulSoup objects using ==.
#     What do you expect the result to be?

# Q15. Find the goal event using a callable filter.
#     Change its description to "Ferran Torres scores the World Cup winning goal".
#     Write the modified HTML to a new file.




scoreboard = soup.find("section",class_="scoreboard")
spain = scoreboard.find("div",class_="team", attrs={"data-country": "Spain"})
score = spain.find("p",class_="score")

#print(score.text)





