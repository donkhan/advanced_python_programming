import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon

# Create figure and axes
fig, ax = plt.subplots(figsize=(6, 8), label="Human Cartoon")
ax.set_aspect('equal')

# -----------------------
# Head
# -----------------------
head = Circle((0, 7), 0.8,
              facecolor='#FFD39B',
              edgecolor='black',
              linewidth=2)
ax.add_patch(head)

# Eyes
left_eye = Circle((-0.25, 7.2), 0.06, color='black')
right_eye = Circle((0.25, 7.2), 0.06, color='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Smile
ax.plot([-0.25, 0, 0.25],
        [6.8, 6.65, 6.8],
        color='red', linewidth=2)

# Hair
hair = Ellipse((0, 7.55),
               width=1.55,
               height=0.55,
               facecolor='black')
ax.add_patch(hair)

# -----------------------
# Neck
# -----------------------
ax.plot([0, 0], [6.2, 5.8],
        color='black', linewidth=4)

# -----------------------
# Body
# -----------------------
shirt = Polygon([
    (-0.8, 5.8),
    (0.8, 5.8),
    (1.0, 3.2),
    (-1.0, 3.2)
], closed=True,
   facecolor='skyblue',
   edgecolor='black',
   linewidth=2)

ax.add_patch(shirt)

# -----------------------
# Arms
# -----------------------
ax.plot([-0.8, -2.0],
        [5.5, 4.0],
        linewidth=5,
        color='black')

ax.plot([0.8, 2.0],
        [5.5, 4.0],
        linewidth=5,
        color='black')

# Hands
ax.add_patch(Circle((-2.0, 4.0), 0.15,
                    facecolor='#FFD39B',
                    edgecolor='black'))

ax.add_patch(Circle((2.0, 4.0), 0.15,
                    facecolor='#FFD39B',
                    edgecolor='black'))

# -----------------------
# Pants
# -----------------------
pants = Polygon([
    (-1.0, 3.2),
    (1.0, 3.2),
    (0.7, 1.2),
    (-0.7, 1.2)
], closed=True,
   facecolor='navy',
   edgecolor='black',
   linewidth=2)

ax.add_patch(pants)

# -----------------------
# Legs
# -----------------------
ax.plot([-0.35, -0.6],
        [1.2, -1],
        linewidth=6,
        color='black')

ax.plot([0.35, 0.6],
        [1.2, -1],
        linewidth=6,
        color='black')

# Shoes
ax.plot([-0.8, -0.4],
        [-1.0, -1.0],
        linewidth=7,
        color='brown')

ax.plot([0.4, 0.8],
        [-1.0, -1.0],
        linewidth=7,
        color='brown')

# -----------------------
# Final formatting
# -----------------------
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 9)

ax.set_xticks([])
ax.set_yticks([])

ax.set_title("Human Figure Drawn with Matplotlib", fontsize=16)

plt.show()