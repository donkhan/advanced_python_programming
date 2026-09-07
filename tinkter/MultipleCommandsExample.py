import tkinter as tk
from tkinter import ttk


def change_font_size(value):
    lbl.config(font=(font_var.get(), int(float(value))))


def change_font(event):
    lbl.config(font=(font_var.get(), slider.get()))


fonts = ["Arial", "Calibri", "Times New Roman", "Courier New", "Verdana"]

# Create the main window
root = tk.Tk()
root.title("Font Size Demo")
root.geometry("400x200")

# Label
lbl = tk.Label(root, text="Advanced Python", font=("Arial", 20))
lbl.pack(pady=20)

# Slider
slider = tk.Scale(root, from_=10, to=50,
                  orient="horizontal", label="Font Size",
                  command=change_font_size)
slider.set(20)
slider.pack()
slider.focus()

font_var = tk.StringVar(value="Arial")

font_box = ttk.Combobox(
    root,
    textvariable=font_var,
    values=fonts,
    state="readonly"
)

font_box.bind("<<ComboboxSelected>>", change_font)
font_box.pack(pady=10)

# Start the event loop
root.mainloop()