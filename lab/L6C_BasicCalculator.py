import tkinter as tk


def add():
    answer.config(text="Sum of  " + operand_1.get() + " and " + operand_2.get() + " is "
                       + str(int(operand_1.get()) + int(operand_2.get())))


def subtract():
    answer.config(text="Difference of  " + operand_1.get() + " and " + operand_2.get() + " is "
                       + str(int(operand_1.get()) - int(operand_2.get())))


def multiply():
    answer.config(text="Multiplication of  " + operand_1.get() + " and " + operand_2.get() + " is "
                       + str(int(operand_1.get()) * int(operand_2.get())))


def divide():
    answer.config(text="Division of  " + operand_1.get() + " and " + operand_2.get() + " is "
                       + str(int(operand_1.get()) % int(operand_2.get())))


root = tk.Tk()
root.title("Basic Calculator")
root.geometry("500x300")
root.resizable(False, False)

label = tk.Label(root, text="Basic Calculator")
label.pack()

label = tk.Label(root, text="Operand-1")
label.pack()

operand_1 = tk.Entry(root)
operand_1.pack()
operand_1.focus_set()

label = tk.Label(root, text="Operand-2")
label.pack()

operand_2 = tk.Entry(root)
operand_2.pack()

button = tk.Button(root, text="Add + ", command=add)
button.pack()

button = tk.Button(root, text="Sub - ", command=subtract)
button.pack()

button = tk.Button(root, text="Multiply * ", command=multiply)
button.pack()

button = tk.Button(root, text="Divide % ", command=divide)
button.pack()


answer = tk.Label(root, text="Answer...")
answer.pack()


root.mainloop()