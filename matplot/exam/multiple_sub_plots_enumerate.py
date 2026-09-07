import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 500)

functions = [
    np.sin,
    np.cos,
    np.tan,
    lambda x: 1/np.tan(x),
    lambda x: 1/np.cos(x),
    lambda x: 1/np.sin(x),
    np.arcsin,
    np.arccos,
    np.arctan
]

titles = ["sin(x)", "cos(x)", "tan(x)",
          "cot(x)", "sec(x)", "csc(x)",
          "Sin Inverse", "Cos Inverse", "Tan Inverse"]

plt.figure(figsize=(10, 8),label="Showing all trigonometric functions")
for i, (func, title) in enumerate(zip(functions, titles), start=1):
    plt.subplot(3, 3, i)
    plt.plot(x, func(x))
    plt.title(title)
    if title in ("tan(x)", "cot(x)", "sec(x)", "csc(x)"):
        plt.ylim(-5, 5)
    plt.grid()

plt.tight_layout()
plt.show()