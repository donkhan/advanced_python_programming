import numpy as np
import matplotlib.pyplot as plt

# Required for 3D plotting
from mpl_toolkits.mplot3d import Axes3D

# Generate data
t = np.linspace(0, 10*np.pi, 500)

x = np.cos(t)
y = np.sin(t)
z = t

# Create figure
fig = plt.figure(figsize=(8,6))

# Add 3D axes
ax = fig.add_subplot(111, projection='3d')

# Plot 3D line
ax.plot(x, y, z,
        color="blue",
        linewidth=2,
        label="Helix")

# Labels
ax.set_title("3D Helix")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

ax.legend()
ax.grid(True)

plt.show()