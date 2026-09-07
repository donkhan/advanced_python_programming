from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
        pass


root = Tk()
s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
#mainframe = ttk.Frame(root, width=200, height=200, style='Danger.TFrame')

root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

feet = StringVar()
#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry= ttk.Spinbox(mainframe, from_=1.0, to=100.0, textvariable=feet)
#feet_entry = ttk.Scale(mainframe, orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=feet)

feet_entry.grid(column=2, row=1, sticky=(W, E))


meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#countryvar = StringVar()
#country = ttk.Combobox(mainframe, textvariable=countryvar)
#country['values'] = ('USA', 'Canada', 'Australia')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
#country.focus()

root.bind("<Return>", calculate)

root.mainloop()
