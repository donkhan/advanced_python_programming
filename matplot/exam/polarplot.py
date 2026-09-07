import numpy as np
import matplotlib.pyplot as plt

# Cartesian coordinates
x = np.array([2, 2, 0, -2, -3, -2, 0, 2, 4, 3])
y = np.array([0, 2, 3, 2, 0, -2, -4, -2, 0, 3])

# Convert to Polar
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

# Create two subplots
fig = plt.figure(figsize=(12, 6),label="Cartesian Vs Polar")

cartesian_axis = plt.subplot(1, 2, 1)
cartesian_axis.scatter(x, y, s=80)

for i in range(len(x)):
    cartesian_axis.text(x[i] + 0.1, y[i] + 0.1, f"P{i + 1}")

cartesian_axis.axhline(0, color='black')
cartesian_axis.axvline(0, color='black')
cartesian_axis.grid(True)

cartesian_axis.set(title="K Cartesian", xlabel="X", ylabel="Y", aspect='equal')

polar_axis = plt.subplot(1, 2, 2, projection='polar')
polar_axis.scatter(theta, r)

for i in range(len(r)):
    polar_axis.text(theta[i], r[i] + 0.2, f"P{i + 1}")
    
polar_axis.set_title("Polar Coordinates")

plt.tight_layout()
plt.show()