import tkinter as tk
import time

root = tk.Tk()
root.geometry("400x200")

label = tk.Label(root, text="Waiting...")
label.pack()

def work():
    label.config(text="Working...")
    root.update()      # Try removing this line
    time.sleep(5)
    label.config(text="Finished")

tk.Button(root, text="Start", command=work).pack()

root.mainloop()