import customtkinter as ctk

# -------------------------------
# Initial Configuration
# -------------------------------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Widget Scaling Demo")
root.geometry("500x400")

# -------------------------------
# Event Handler
# -------------------------------
def change_scaling(value):
    percentage = int(value)
    ctk.set_widget_scaling(percentage / 100)
    scaling_label.configure(text=f"Widget Scaling : {percentage}%")

# -------------------------------
# Widgets
# -------------------------------
heading = ctk.CTkLabel(
    root,
    text="CustomTkinter Widget Scaling",
    font=("Arial", 22, "bold")
)
heading.pack(pady=20)

name_entry = ctk.CTkEntry(root, width=250, placeholder_text="Enter your name")
name_entry.pack(pady=10)

password_entry = ctk.CTkEntry(
    root,
    width=250,
    placeholder_text="Enter password",
    show="*"
)
password_entry.pack(pady=10)

submit_button = ctk.CTkButton(root, text="Submit")
submit_button.pack(pady=10)

remember_checkbox = ctk.CTkCheckBox(root, text="Remember Me")
remember_checkbox.pack(pady=10)

scaling_label = ctk.CTkLabel(root, text="Widget Scaling : 100%")
scaling_label.pack(pady=(20, 5))

slider = ctk.CTkSlider(
    root,
    from_=50,
    to=200,
    number_of_steps=15,
    command=change_scaling
)
slider.set(100)
slider.pack(padx=30, fill="x")

root.mainloop()