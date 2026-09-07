import tkinter as tk


# Callback function
def change_font_size(value):
    lbl.config(font=("Arial", int(float(value))))


# Create the main window
root = tk.Tk()
root.title("Font Size Demo")
root.geometry("400x200")

# Label
lbl = tk.Label(root, text="Advanced Python", font=("Arial", 20))
lbl.pack(pady=20)

# Slider
slider = tk.Scale(root, from_=10, to=50, orient="horizontal",
                  label="Font Size", command=change_font_size)
slider.set(20)
slider.pack()
slider.focus()

# Start the event loop
root.mainloop()