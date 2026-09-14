import tkinter as tk
from tkinter import ttk


def add_task():
    win = tk.Toplevel(root)
    win.title("Add Task")
    win.geometry("250x150")

    tk.Label(win, text="Task").pack()
    task = tk.Entry(win)
    task.pack()

    tk.Label(win, text="Duration").pack()
    duration = tk.Entry(win)
    duration.pack()

    def save():
        table.insert("", "end", values=(task.get(), duration.get()))
        win.destroy()

    tk.Button(win, text="Add", command=save).pack(pady=10)


def delete_task():
    selected = table.selection()
    if selected:
        table.delete(selected[0])


root = tk.Tk()
root.title("Task Manager")
root.geometry("500x300")
root.resizable(False, False)

label = tk.Label(root, text="Task Manager")
label.pack()

table = ttk.Treeview(root, columns=("Task", "Duration"), show="headings")

table.heading("Task", text="Task")
table.heading("Duration", text="Duration")

table.insert("", "end", values=("Meeting Research Director", "20 mins"))
table.insert("", "end", values=("Meeting IQAC Director", "10 mins"))

table.pack()

button = tk.Button(root, text="Add Task + ", command=add_task)
button.pack()

button = tk.Button(root, text="Delete Task - ", command=delete_task)
button.pack()



root.mainloop()