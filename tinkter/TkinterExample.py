import tkinter as tk

root = tk.Tk()

root.title("Login")
root.geometry("300x200")

label = tk.Label(root, text="Username")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Login")
button.pack(pady=20)

root.mainloop()