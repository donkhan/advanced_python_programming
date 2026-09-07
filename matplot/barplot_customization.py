import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
marks = [92, 85, 78, 88, 81]

bars = plt.bar(
    subjects,
    marks,
    color=["royalblue", "orange", "green", "red", "purple"],
    edgecolor="black",
    linewidth=2,
    width=0.6,
    alpha=0.8
)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 1,
        str(height),
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

plt.title("Subject-wise Marks", fontsize=16, fontweight="bold")
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Marks", fontsize=12)

plt.ylim(0, 100)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()