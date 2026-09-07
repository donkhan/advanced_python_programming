import tkinter as tk


def calculate_bmi(value=None):
    height = height_slider.get() / 100   # cm → metres
    weight = weight_slider.get()         # kg

    bmi = weight / (height ** 2)

    bmi_label.config(text=f"BMI: {bmi:.2f}")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")

# Height
tk.Label(root, text="Height (cm)").pack(pady=10)

height_slider = tk.Scale(
    root,
    from_=100,
    to=220,
    orient="horizontal",
    command=calculate_bmi
)
height_slider.set(170)
height_slider.pack()

# Weight
tk.Label(root, text="Weight (kg)").pack(pady=10)

weight_slider = tk.Scale(
    root,
    from_=30,
    to=150,
    orient="horizontal",
    command=calculate_bmi
)
weight_slider.set(70)
weight_slider.pack()

# BMI
bmi_label = tk.Label(
    root,
    text="BMI: 24.22",
    font=("Arial", 18)
)
bmi_label.pack(pady=20)

root.mainloop()