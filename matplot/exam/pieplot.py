import matplotlib.pyplot as plt

subjects = ["Mathematics", "Physics", "Chemistry",
            "Biology", "English", "Computer Science"]

marks = [95, 85, 80, 70, 60, 110]
plt.figure(figsize=(6,6),label="AC")
plt.pie(marks,
        labels=subjects,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Marks Distribution by Subject")
plt.show()