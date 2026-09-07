import ttkbootstrap as ttk

root = ttk.Window(themename="superhero")

ttk.Button(
    root,
    text="Submit",
    bootstyle="success"
).pack(pady=20)

root.mainloop()