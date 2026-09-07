import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10, 1)
y = np.square(x)

fig, ax = plt.subplots(label="Square Numbers")
ax.plot(x, y)

ax.set(title="SQ of Numbers", xlabel="X",ylabel="Y")
ax.grid()
plt.show()