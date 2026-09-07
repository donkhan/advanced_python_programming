import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(label="Penguin Count Based on Gender")
#fig.canvas.manager.set_window_title("Penguin Count")

species = ('Adelie', 'Chinstrap', 'Gentoo')
counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6
bottom = np.zeros(3)

for gender, count in counts.items():
    p = ax.bar(species, count, width, label=gender, bottom=bottom)
    bottom += count
    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by Gender')
ax.legend()
plt.show()