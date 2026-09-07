import matplotlib.pyplot as plt

# Time-series data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 150, 145, 170, 190]

plt.figure(figsize=(8,5))

plt.plot(
    months,
    sales
)

#plt.title("Monthly Sales")
#plt.xlabel("Month")
#plt.ylabel("Sales (in Units)")

plt.grid(True, linestyle='--', alpha=0.6)

plt.show()