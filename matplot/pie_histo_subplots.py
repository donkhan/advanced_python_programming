import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
subject_marks = [95, 85, 75, 80, 65]

student_marks = [45,52,67,72,81,90,55,60,74,68,
                 88,92,49,53,77,84,61,70,79,95,
                 66,58,73,80,85,91,62,57,69,76]

plt.figure(figsize=(12,5))

# Pie Chart
plt.subplot(1,2,1)
plt.pie(subject_marks,
        labels=subjects,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Subject-wise Marks")

# Histogram
plt.subplot(1,2,2)
plt.hist(student_marks,
         bins=6,
         edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()