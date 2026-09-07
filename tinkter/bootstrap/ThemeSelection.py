import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="cosmo")
root.title("ttkbootstrap Theme Selector")
root.geometry("450x250")

style = ttk.Style()

# Get all available themes
themes = style.theme_names()

ttk.Label(
    root,
    text="Select a Theme:",
    font=("Arial", 12)
).pack(pady=10)

theme_combo = ttk.Combobox(
    root,
    values=themes,
    state="readonly",
    width=25
)
theme_combo.pack(pady=10)

# Show current theme
theme_combo.set(style.theme.name)

def change_theme(event=None):
    selected_theme = theme_combo.get()
    style.theme_use(selected_theme)

theme_combo.bind("<<ComboboxSelected>>", change_theme)

# Sample widgets to demonstrate the theme
ttk.Label(root, text="This is a Label").pack(pady=5)
ttk.Entry(root).pack(pady=5)
ttk.Checkbutton(root, text="Check Me").pack(pady=5)
ttk.Button(root, text="Sample Button", bootstyle=SUCCESS).pack(pady=10)

root.mainloop()