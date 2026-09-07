import tkinter as tk
from tkinter import ttk

# -----------------------------
# Button Event
# -----------------------------
def show_values():
    print("Name      :", entry.get())
    print("Password  :", password.get())
    print("Country   :", combo.get())
    print("Gender    :", gender.get())
    print("Python    :", python_var.get())
    print("Java      :", java_var.get())
    print("Experience:", slider.get())
    print("Comments:")
    print(textbox.get("1.0", tk.END))


# -----------------------------
# Window
# -----------------------------
root = tk.Tk()
root.title("Tkinter Widget Demo")
root.geometry("700x750")

# -----------------------------
# Label
# -----------------------------
tk.Label(
    root,
    text="Tkinter Widget Demo",
    font=("Arial", 20, "bold")
).pack(pady=10)

# -----------------------------
# Entry
# -----------------------------
tk.Label(root, text="Name").pack(anchor="w", padx=20)

entry = tk.Entry(root, width=50)
entry.pack(padx=20, pady=5)

# -----------------------------
# Password
# -----------------------------
tk.Label(root, text="Password").pack(anchor="w", padx=20)

password = tk.Entry(root, width=50, show="*")
password.pack(padx=20, pady=5)

# -----------------------------
# Combobox
# -----------------------------
tk.Label(root, text="Country").pack(anchor="w", padx=20)

combo = ttk.Combobox(
    root,
    values=[
        "India",
        "USA",
        "France",
        "Australia",
        "Germany"
    ]
)

combo.current(0)
combo.pack(padx=20, pady=5)

# -----------------------------
# Radio Buttons
# -----------------------------
tk.Label(root, text="Gender").pack(anchor="w", padx=20)

gender = tk.StringVar(value="Male")

tk.Radiobutton(
    root,
    text="Male",
    variable=gender,
    value="Male"
).pack(anchor="w", padx=40)

tk.Radiobutton(
    root,
    text="Female",
    variable=gender,
    value="Female"
).pack(anchor="w", padx=40)

# -----------------------------
# Check Buttons
# -----------------------------
tk.Label(root, text="Programming Languages").pack(anchor="w", padx=20)

python_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Python",
    variable=python_var
).pack(anchor="w", padx=40)

java_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Java",
    variable=java_var
).pack(anchor="w", padx=40)

# -----------------------------
# Scale
# -----------------------------
tk.Label(root, text="Experience").pack(anchor="w", padx=20)

slider = tk.Scale(
    root,
    from_=0,
    to=20,
    orient="horizontal"
)

slider.pack(fill="x", padx=20)

# -----------------------------
# Progress Bar
# -----------------------------
tk.Label(root, text="Progress").pack(anchor="w", padx=20)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=400,
    mode="determinate"
)

progress["value"] = 70
progress.pack(fill="x", padx=20)

# -----------------------------
# Text Box
# -----------------------------
tk.Label(root, text="Comments").pack(anchor="w", padx=20)

textbox = tk.Text(
    root,
    width=70,
    height=6
)

textbox.pack(padx=20, pady=10)

# -----------------------------
# Buttons
# -----------------------------
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(
    frame,
    text="Submit",
    command=show_values
).pack(side="left", padx=10)

tk.Button(
    frame,
    text="Exit",
    command=root.destroy
).pack(side="left", padx=10)

# -----------------------------
# Start GUI
# -----------------------------
root.mainloop()