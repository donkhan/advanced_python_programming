import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 10 Complex Numbers
# -------------------------------------------------
z = np.array([
    1+0j,
    -1+0j,
    0+1j,
    0-1j,
    1+1j,
    -1+1j,
    -1-1j,
    1-1j,
    2+1j,
    -2+2j
])

labels = [
    "1",
    "-1",
    "i",
    "-i",
    "1+i",
    "-1+i",
    "-1-i",
    "1-i",
    "2+i",
    "-2+2i"
]

# Cartesian coordinates
x = z.real
y = z.imag

# Polar coordinates
r = np.abs(z)          # Magnitude
theta = np.angle(z)    # Angle (radians)

plt.figure(figsize=(12,6), label="Test")
plt.subplot(1,2,1)
plt.scatter(x, y, s=80)

for i in range(len(z)):
    plt.text(x[i]+0.05, y[i]+0.05, labels[i])

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.grid(True)
plt.axis('equal')

plt.title("Complex Numbers (Cartesian Form)")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")

plt.subplot(1,2,2, projection='polar')
plt.scatter(theta, r, s=80)
for i in range(len(z)):
    plt.text(theta[i], r[i]+0.15, labels[i])

plt.title("Complex Numbers (Polar Form)")
plt.tight_layout()
plt.show()