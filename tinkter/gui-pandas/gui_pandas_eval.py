import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

chocolate = None


def show_dataframe(data):

    # Clear old rows
    tree.delete(*tree.get_children())

    # Remove old columns
    tree["columns"] = list(data.columns)
    tree["show"] = "headings"

    # Create headings
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    # Insert rows
    for row in data.itertuples(index=False):
        tree.insert("", tk.END, values=row)


def load_csv():
    global chocolate

    filename = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not filename:
        return

    try:
        chocolate = pd.read_csv(filename)
        chocolate = chocolate.head(100)
        chocolate.rename(columns={"Company Location": "Location"}, inplace=True)
        chocolate["Cocoa Percent"] = chocolate["Cocoa Percent"].str.rstrip("%").astype(float)

        show_dataframe(chocolate)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def execute_query():
    global chocolate

    if chocolate is None:
        messagebox.showwarning("Warning", "Please load a CSV file first.")
        return

    expr = query.get("1.0", tk.END).strip()

    if expr == "":
        return

    try:
        # 'chocolate' is available inside eval()
        result = eval(expr, {"pd": pd}, {"chocolate": chocolate})

        if isinstance(result, pd.DataFrame):
            show_dataframe(result)
        elif isinstance(result, pd.Series):
            show_dataframe(result.to_frame())
        else:
            messagebox.showinfo("Result", str(result))

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Mini Pandas Explorer")
root.geometry("1000x600")

top = tk.Frame(root)
top.pack(fill="x", padx=10, pady=5)

tk.Button(top, text="Load CSV", command=load_csv).pack(side="left")

tk.Label(root, text="Enter Pandas Expression (use variable 'chocolate')").pack()

query = tk.Text(root, height=4)
query.pack(fill="x", padx=10)

query.insert("1.0", 'chocolate.head()')

tk.Button(root, text="Execute", command=execute_query).pack(pady=5)

tree = ttk.Treeview(root)

scroll_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll_y.set)

scroll_y.pack(side="right", fill="y")
tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()