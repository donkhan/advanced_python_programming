import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
z = [0, 4, 2, 5, 3]

# Create figure
fig = plt.figure(figsize=(8,6))

# Create 3D axes
ax = fig.add_subplot(111, projection='3d')

# Draw 3D line
ax.plot(x, y, z,
        color='blue',
        linewidth=2,
        marker='o')

# Labels
ax.set_title("Simple 3D Line Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

plt.show()