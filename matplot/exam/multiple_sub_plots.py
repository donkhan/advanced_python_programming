import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 500)

plt.figure(figsize=(10, 8))

plt.subplot(3, 2, 1)
plt.plot(x, np.sin(x))
plt.title("sin(x)")
plt.grid()

plt.subplot(3, 2, 2)
plt.plot(x, np.cos(x))
plt.title("cos(x)")
plt.grid()

plt.subplot(3, 2, 3)
plt.plot(x, np.tan(x))
plt.title("tan(x)")
plt.ylim(-5, 5)
plt.grid()

plt.subplot(3, 2, 4)
plt.plot(x, 1/np.tan(x))
plt.title("cot(x)")
plt.ylim(-5, 5)
plt.grid()

plt.subplot(3, 2, 5)
plt.plot(x, 1/np.cos(x))
plt.title("sec(x)")
plt.ylim(-5, 5)
plt.grid()

plt.subplot(3, 2, 6)
plt.plot(x, 1/np.sin(x))
plt.title("csc(x)")
plt.ylim(-5, 5)
plt.grid()

plt.tight_layout()
plt.show()