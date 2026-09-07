import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# ------------------------------
# Button Events
# ------------------------------
def show_values():
    print("Name     :", entry.get())
    print("Password :", password.get())
    print("Gender   :", gender.get())
    print("Country  :", country.get())
    print("Python   :", python_var.get())
    print("Java     :", java_var.get())
    print("Slider   :", slider.get())
    print("Comments :")
    print(text.get("1.0", END))


# ------------------------------
# Window
# ------------------------------
app = ttk.Window(
    title="ttkbootstrap Widget Demo",
    themename="cyborg",
    size=(700, 700)
)

# ------------------------------
# Label
# ------------------------------
ttk.Label(
    app,
    text="ttkbootstrap Widget Demo",
    font=("Arial", 18, "bold"),
    bootstyle="primary"
).pack(pady=10)

# ------------------------------
# Entry
# ------------------------------
ttk.Label(app, text="Name").pack(anchor=W, padx=20)
entry = ttk.Entry(app, width=40)
entry.pack(padx=20, fill=X)

# ------------------------------
# Password
# ------------------------------
ttk.Label(app, text="Password").pack(anchor=W, padx=20)
password = ttk.Entry(app, width=40, show="*")
password.pack(padx=20, fill=X)

# ------------------------------
# Combobox
# ------------------------------
ttk.Label(app, text="Country").pack(anchor=W, padx=20)

country = ttk.Combobox(
    app,
    values=[
        "India",
        "USA",
        "France",
        "Australia",
        "Germany"
    ]
)

country.current(0)
country.pack(padx=20, fill=X)

# ------------------------------
# Radio Buttons
# ------------------------------
ttk.Label(app, text="Gender").pack(anchor=W, padx=20)

gender = ttk.StringVar(value="Male")

ttk.Radiobutton(
    app,
    text="Male",
    variable=gender,
    value="Male",
    bootstyle="primary"
).pack(anchor=W, padx=40)

ttk.Radiobutton(
    app,
    text="Female",
    variable=gender,
    value="Female",
    bootstyle="primary"
).pack(anchor=W, padx=40)

# ------------------------------
# Checkbuttons
# ------------------------------
ttk.Label(app, text="Programming Languages").pack(anchor=W, padx=20)

python_var = ttk.BooleanVar()
java_var = ttk.BooleanVar()

ttk.Checkbutton(
    app,
    text="Python",
    variable=python_var,
    bootstyle="success-round-toggle"
).pack(anchor=W, padx=40)

ttk.Checkbutton(
    app,
    text="Java",
    variable=java_var,
    bootstyle="success-round-toggle"
).pack(anchor=W, padx=40)

# ------------------------------
# Scale
# ------------------------------
ttk.Label(app, text="Experience").pack(anchor=W, padx=20)

slider = ttk.Scale(
    app,
    from_=0,
    to=20,
    bootstyle="info"
)

slider.pack(fill=X, padx=20)

# ------------------------------
# Progressbar
# ------------------------------
ttk.Label(app, text="Progress").pack(anchor=W, padx=20)

progress = ttk.Progressbar(
    app,
    value=70,
    bootstyle="success-striped"
)

progress.pack(fill=X, padx=20)

# ------------------------------
# Text
# ------------------------------
ttk.Label(app, text="Comments").pack(anchor=W, padx=20)

text = ttk.Text(app, height=5)

text.pack(fill=BOTH, padx=20)

# ------------------------------
# Buttons
# ------------------------------
frame = ttk.Frame(app)
frame.pack(pady=15)

ttk.Button(
    frame,
    text="Submit",
    command=show_values,
    bootstyle="success"
).pack(side=LEFT, padx=10)

ttk.Button(
    frame,
    text="Cancel",
    command=app.destroy,
    bootstyle="danger"
).pack(side=LEFT, padx=10)

app.mainloop()