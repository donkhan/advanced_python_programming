import customtkinter as ctk

ctk.set_appearance_mode("System")      # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")

mainframe = ctk.CTk()

mainframe.geometry("300x200")

button = ctk.CTkButton(mainframe, text="Click Me")
button.pack(pady=40)

mainframe.mainloop()