import matplotlib.pyplot as plt

# Years
years = [2021, 2022, 2023, 2024, 2025]

# Heights (cm)
amit  = [150, 155, 160, 165, 168]
priya = [148, 152, 156, 160, 163]
rahul = [152, 158, 164, 170, 174]

plt.figure(figsize=(8,5))

plt.plot(years, amit,
         color="blue",
         marker="o",
         linestyle="-",
         linewidth=2,
         label="Amit")

plt.plot(years, priya,
         color="red",
         marker="s",
         linestyle="--",
         linewidth=2,
         label="Priya")

plt.plot(years, rahul,
         color="green",
         marker="^",
         linestyle=":",
         linewidth=2,
         label="Rahul")

plt.title("Height Growth of Students")
plt.xlabel("Year")
plt.ylabel("Height (cm)")

plt.legend()
plt.grid(True)

plt.show()