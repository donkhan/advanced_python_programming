import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch

# ---------------- Data ----------------

pie_labels = ["Approve", "Disapprove", "Undecided"]
pie_values = [27, 56, 17]

age_labels = ["<35", "35-49", "50-65", ">65"]

age_data = {
    "Approve":    [33, 54, 7, 6],
    "Disapprove": [20, 30, 35, 15],
    "Undecided":  [25, 25, 25, 25]
}

# ---------------- Figure ----------------

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,5))
fig.subplots_adjust(wspace=0.35)

wedges, texts, autotexts = ax1.pie(
    pie_values,
    labels=pie_labels,
    autopct="%1.0f%%",
    startangle=90,
    explode=[0.05,0,0]
)

ax1.set_title("Opinion Poll")

connector1 = None
connector2 = None


# ---------------- Draw Bar ----------------

def draw_bar(category):

    ax2.clear()

    values = age_data[category]

    bars = ax2.bar(age_labels, values, color="skyblue")

    ax2.set_ylim(0,60)
    ax2.set_ylabel("Percentage")
    ax2.set_title(category)

    for b in bars:
        h = b.get_height()
        ax2.text(
            b.get_x()+b.get_width()/2,
            h+1,
            f"{h}%",
            ha="center"
        )


# ---------------- Draw Connectors ----------------

def draw_connectors(index):

    global connector1, connector2

    if connector1:
        connector1.remove()

    if connector2:
        connector2.remove()

    wedge = wedges[index]

    theta1 = np.deg2rad(wedge.theta1)
    theta2 = np.deg2rad(wedge.theta2)

    cx, cy = wedge.center
    r = wedge.r

    x1 = cx + r*np.cos(theta1)
    y1 = cy + r*np.sin(theta1)

    x2 = cx + r*np.cos(theta2)
    y2 = cy + r*np.sin(theta2)

    connector1 = ConnectionPatch(
        xyA=(-0.45,60),
        coordsA=ax2.transData,
        xyB=(x2,y2),
        coordsB=ax1.transData,
        color="black",
        linewidth=2
    )

    connector2 = ConnectionPatch(
        xyA=(-0.45,0),
        coordsA=ax2.transData,
        xyB=(x1,y1),
        coordsB=ax1.transData,
        color="black",
        linewidth=2
    )

    fig.add_artist(connector1)
    fig.add_artist(connector2)


# ---------------- Highlight ----------------

def highlight(index):

    for w in wedges:
        w.set_alpha(0.4)
        w.set_linewidth(1)

    wedges[index].set_alpha(1)
    wedges[index].set_edgecolor("red")
    wedges[index].set_linewidth(3)


# ---------------- Click Event ----------------

def onclick(event):

    if event.inaxes != ax1:
        return

    for i, wedge in enumerate(wedges):

        if wedge.contains(event)[0]:

            category = pie_labels[i]

            highlight(i)
            draw_bar(category)
            draw_connectors(i)

            fig.canvas.draw_idle()

            break


# ---------------- Initial Display ----------------

highlight(0)
draw_bar("Approve")
draw_connectors(0)

fig.canvas.mpl_connect("button_press_event", onclick)

plt.show()