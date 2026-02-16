import tkinter as tk
from tkinter import ttk, messagebox
from core import convert


def perform_conversion():
    try:
        value = float(value_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        result = convert(value, from_unit, to_unit)
        result_label.config(text=f"Result: {result:.4f} {to_unit}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x500")


tk.Label(root, text="Enter Value:").pack(pady=5)
value_entry = tk.Entry(root)
value_entry.pack()


tk.Label(root, text="From Unit:").pack(pady=5)
from_unit_var = tk.StringVar()
from_unit_dropdown = ttk.Combobox(
    root,
    textvariable=from_unit_var,
    values=["kg", "lb", "oz", "ml", "m", "ft"],
    state="readonly"
)
from_unit_dropdown.pack()


tk.Label(root, text="To Unit:").pack(pady=5)
to_unit_var = tk.StringVar()
to_unit_dropdown = ttk.Combobox(
    root,
    textvariable=to_unit_var,
    values=["kg", "lb", "oz", "ml", "m", "ft"],
    state="readonly"
)
to_unit_dropdown.pack()


tk.Button(root, text="Convert", command=perform_conversion).pack(pady=15)

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
