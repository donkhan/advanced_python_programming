import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd


def load_csv():
    filename = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not filename:
        return

    df = pd.read_csv(filename)

    # Clear previous data
    tree.delete(*tree.get_children())

    # Remove old columns
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    # Create headings
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    # Insert data
    for row in df.itertuples(index=False):
        tree.insert("", tk.END, values=row)


# ---------------- GUI ----------------

root = tk.Tk()
root.title("CSV Viewer using Pandas")
root.geometry("800x500")

btn = tk.Button(root, text="Load CSV", command=load_csv)
btn.pack(pady=10)

tree = ttk.Treeview(root)
tree.pack(fill="both", expand=True)

root.mainloop()