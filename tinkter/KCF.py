import tkinter as tk

updating = False


def update_temperature(source, value):
    global updating

    if updating:
        return

    updating = True

    value = float(value)

    # Convert selected scale to Celsius
    if source == "C":
        c = value

    elif source == "F":
        c = (value - 32) * 5 / 9

    else:
        c = value - 273.15

    # Convert Celsius to other scales
    f = c * 9 / 5 + 32
    k = c + 273.15

    # Update sliders
    celsius_slider.set(c)
    fahrenheit_slider.set(f)
    kelvin_slider.set(k)

    # Display all three values
    value_label.config(
        text=f"{c:.1f} °C    =    {f:.1f} °F    =    {k:.1f} K"
    )

    # Interesting physical temperatures
    status = ""

    if abs(c + 273.15) <= 3:
        status = "Absolute Zero"

    elif abs(c - 0) <= 3:
        status = "❄ Freezing Point of Water"

    elif abs(c - 4) <= 3:
        status = "💧 Water has Maximum Density"

    elif abs(c - 25) <= 3:
        status = "Room Temperature"

    elif abs(c - 37) <= 3:
        status = "🌡 Human Body Temperature"

    elif abs(c - 100) <= 3:
        status = "♨ Boiling Point of Water"

    elif abs(c - 660) <= 5:
        status = "Aluminium Melts"

    elif abs(c - 1538) <= 8:
        status = "Iron Melts"

    else:
        status = ""

    status_label.config(text=status)

    updating = False


root = tk.Tk()
root.title("Temperature Explorer")
root.geometry("650x600")


# =========================================================
# Celsius
# =========================================================

tk.Label(
    root,
    text="Celsius (°C)",
    font=("Arial", 12, "bold")
).pack(pady=(15, 0))

celsius_slider = tk.Scale(
    root,
    from_=-300,
    to=1600,
    resolution=1,
    tickinterval=200,
    orient="horizontal",
    length=550,
    command=lambda value: update_temperature("C", value)
)

celsius_slider.set(25)
celsius_slider.pack()


# =========================================================
# Fahrenheit
# =========================================================

tk.Label(
    root,
    text="Fahrenheit (°F)",
    font=("Arial", 12, "bold")
).pack(pady=(15, 0))

fahrenheit_slider = tk.Scale(
    root,
    from_=-500,
    to=3000,
    resolution=1,
    tickinterval=500,
    orient="horizontal",
    length=550,
    command=lambda value: update_temperature("F", value)
)

fahrenheit_slider.set(77)
fahrenheit_slider.pack()


# =========================================================
# Kelvin
# =========================================================

tk.Label(
    root,
    text="Kelvin (K)",
    font=("Arial", 12, "bold")
).pack(pady=(15, 0))

kelvin_slider = tk.Scale(
    root,
    from_=0,
    to=1900,
    resolution=1,
    tickinterval=200,
    orient="horizontal",
    length=550,
    command=lambda value: update_temperature("K", value)
)

kelvin_slider.set(298)
kelvin_slider.pack()


# =========================================================
# Temperature values
# =========================================================

value_label = tk.Label(
    root,
    text="25.0 °C    =    77.0 °F    =    298.0 K",
    font=("Arial", 17, "bold")
)

value_label.pack(pady=25)


# =========================================================
# Physical phenomenon
# =========================================================

status_label = tk.Label(
    root,
    text="Room Temperature",
    font=("Arial", 15)
)

status_label.pack()


root.mainloop()