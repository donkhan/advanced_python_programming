import tkinter as tk

def update_label(event):
    lbl.config(text=entry.get())

root = tk.Tk()
root.title("Live Text Demo")
root.geometry("400x200")

lbl = tk.Label(root, text="Type something...", font=("Arial", 20))
lbl.pack(pady=20)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack()

entry.bind("<KeyRelease>", update_label)

root.mainloop()