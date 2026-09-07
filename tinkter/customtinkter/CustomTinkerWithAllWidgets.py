import customtkinter as ctk

# -----------------------------
# Theme
# -----------------------------
ctk.set_appearance_mode("System")     # Light / Dark / System
ctk.set_default_color_theme("blue")   # blue / green / dark-blue


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
    print(textbox.get("1.0", "end"))


# -----------------------------
# Window
# -----------------------------
app = ctk.CTk()
app.title("CustomTkinter Widget Demo")
app.geometry("700x750")

# -----------------------------
# Label
# -----------------------------
ctk.CTkLabel(
    app,
    text="CustomTkinter Widget Demo",
    font=("Arial", 22, "bold")
).pack(pady=10)

# -----------------------------
# Entry
# -----------------------------
ctk.CTkLabel(app, text="Name").pack(anchor="w", padx=20)

entry = ctk.CTkEntry(app, width=500)
entry.pack(padx=20, pady=5)

# -----------------------------
# Password
# -----------------------------
ctk.CTkLabel(app, text="Password").pack(anchor="w", padx=20)

password = ctk.CTkEntry(app, width=500, show="*")
password.pack(padx=20, pady=5)

# -----------------------------
# Combo Box
# -----------------------------
ctk.CTkLabel(app, text="Country").pack(anchor="w", padx=20)

combo = ctk.CTkComboBox(
    app,
    values=[
        "India",
        "USA",
        "France",
        "Australia",
        "Germany"
    ]
)

combo.pack(padx=20, pady=5)

# -----------------------------
# Radio Buttons
# -----------------------------
ctk.CTkLabel(app, text="Gender").pack(anchor="w", padx=20)

gender = ctk.StringVar(value="Male")

ctk.CTkRadioButton(
    app,
    text="Male",
    variable=gender,
    value="Male"
).pack(anchor="w", padx=40)

ctk.CTkRadioButton(
    app,
    text="Female",
    variable=gender,
    value="Female"
).pack(anchor="w", padx=40)

# -----------------------------
# Check Boxes
# -----------------------------
ctk.CTkLabel(app, text="Programming Languages").pack(anchor="w", padx=20)

python_var = ctk.BooleanVar()

ctk.CTkCheckBox(
    app,
    text="Python",
    variable=python_var
).pack(anchor="w", padx=40)

java_var = ctk.BooleanVar()

ctk.CTkCheckBox(
    app,
    text="Java",
    variable=java_var
).pack(anchor="w", padx=40)

# -----------------------------
# Slider
# -----------------------------
ctk.CTkLabel(app, text="Experience").pack(anchor="w", padx=20)

slider = ctk.CTkSlider(
    app,
    from_=0,
    to=20
)

slider.pack(fill="x", padx=20, pady=10)

# -----------------------------
# Progress Bar
# -----------------------------
ctk.CTkLabel(app, text="Progress").pack(anchor="w", padx=20)

progress = ctk.CTkProgressBar(app)

progress.pack(fill="x", padx=20)
progress.set(0.70)

# -----------------------------
# Text Box
# -----------------------------
ctk.CTkLabel(app, text="Comments").pack(anchor="w", padx=20)

textbox = ctk.CTkTextbox(
    app,
    width=600,
    height=120
)

textbox.pack(padx=20, pady=10)

# -----------------------------
# Buttons
# -----------------------------
frame = ctk.CTkFrame(app)
frame.pack(pady=20)

ctk.CTkButton(
    frame,
    text="Submit",
    command=show_values
).pack(side="left", padx=10)

ctk.CTkButton(
    frame,
    text="Exit",
    fg_color="red",
    hover_color="darkred",
    command=app.destroy
).pack(side="left", padx=10)

app.mainloop()