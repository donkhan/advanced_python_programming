import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
rainfall = [20, 15, 35, 50, 80, 120]

plt.plot(months, rainfall)

plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall")

plt.show()