import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)
r = np.cos(5 * theta)

ax = plt.subplot(projection='polar')
ax.plot(theta, r, linewidth=3)
ax.set_title("Rose Curve")

plt.show()