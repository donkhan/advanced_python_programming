import tkinter as tk


def calculate():
    r = float(entry.get())
    a = 3.14 * r * r
    answer.config(text="Area of circle with radius " + entry.get() + " is " + str(a))


root = tk.Tk()
root.title("Area Calculator")
root.geometry("500x300")
root.resizable(False,False)

label = tk.Label(root, text="Enter the Radius...")
label.pack()

entry = tk.Entry(root)
entry.pack()
entry.focus_set()

answer = tk.Label(root, text="Answer...")
answer.pack()

button = tk.Button(root, text="Calculate  Area", command=calculate)
button.pack()

root.mainloop()