import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import pandas as pd

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


chocolate = None
current_data = None


def show_dataframe(data):
    global current_data
    current_data = data
    tree.delete(*tree.get_children())
    tree["columns"] = list(data.columns)
    tree["show"] = "headings"
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")
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
        chocolate.rename(
            columns={"Company Location": "Location"},
            inplace=True
        )
        chocolate["Cocoa Percent"] = (
            chocolate["Cocoa Percent"]
            .str.rstrip("%")
            .astype(float)
        )
        show_dataframe(chocolate)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def execute_query():
    global chocolate
    if chocolate is None:
        messagebox.showwarning(
            "Warning",
            "Please load a CSV file first."
        )
        return
    expr = query.get("1.0", tk.END).strip()
    if expr == "":
        return
    try:
        result = eval(
            expr,
            {"pd": pd},
            {"chocolate": chocolate}
        )
        if isinstance(result, pd.DataFrame):
            show_dataframe(result)
        elif isinstance(result, pd.Series):
            show_dataframe(result.to_frame())
        else:
            messagebox.showinfo("Result", str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def plot_locations():
    global current_data
    if current_data is None:
        messagebox.showwarning(
            "Warning",
            "No data available."
        )
        return
    if "Location" not in current_data.columns:
        messagebox.showwarning(
            "Warning",
            "Current dataframe must contain a 'Location' column."
        )
        return
    counts = current_data["Location"].value_counts().head(10)
    # Clear previous chart
    for widget in chart_frame.winfo_children():
        widget.destroy()
    fig = Figure(figsize=(7, 4), dpi=100)
    ax = fig.add_subplot(111)
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Top Company Locations")
    ax.set_xlabel("Location")
    ax.set_ylabel("Number of Chocolates")
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


root = tk.Tk()
root.title("Mini Pandas Explorer with Visualization")
root.geometry("1200x800")

top = tk.Frame(root)
top.pack(fill="x", padx=10, pady=5)

tk.Button(
    top,
    text="Load CSV",
    command=load_csv,
    width=15
).pack(side="left", padx=5)

tk.Button(
    top,
    text="Execute",
    command=execute_query,
    width=15
).pack(side="left", padx=5)

tk.Button(
    top,
    text="Plot Locations",
    command=plot_locations,
    width=15
).pack(side="left", padx=5)

tk.Label(
    root,
    text="Enter Pandas Expression (use variable 'chocolate')"
).pack()

query = tk.Text(root, height=4)
query.pack(fill="x", padx=10)

query.insert(
    "1.0",
    "chocolate.head()"
)

tree_frame = tk.Frame(root)
tree_frame.pack(fill="both", expand=True)

tree = ttk.Treeview(tree_frame)
scroll_y = ttk.Scrollbar(
    tree_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(
    yscrollcommand=scroll_y.set
)

scroll_y.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

chart_frame = tk.LabelFrame(
    root,
    text="Matplotlib Chart"
)

chart_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

root.mainloop()