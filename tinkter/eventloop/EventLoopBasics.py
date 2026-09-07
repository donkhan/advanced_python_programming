import tkinter as tk
import time


def long_task():
    print("Started")
    time.sleep(5)
    print("Finished")


def task(remaining):
    print("Started")
    if remaining == 0:
        print("Finished")
        return
    print("Working")
    remaining -= 1
    root.after(100, lambda: task(remaining-1))


root = tk.Tk()

# Avoid long_task method. Instead follow task method
#b1 = tk.Button(root, text="Task", command=long_task)
b1 = tk.Button(root, text="Task", command=lambda: task(50))
b1.pack()
b2 = tk.Button(root, text="Another Button", command=lambda: print("Clicked"))
b2.pack()
root.geometry("400x180")
root.mainloop()