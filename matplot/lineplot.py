import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Sin theta the Nemesis')
ax.grid()

ax.set_title("Sine Wave",fontsize=16,fontweight='bold')


#fig.savefig("test.png")
plt.show()