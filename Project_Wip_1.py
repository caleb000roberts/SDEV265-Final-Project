import tkinter as tk
from tkinter import messagebox
import random

# School supply data
supplies = {
    "Notebooks": 100,
    "Pens": 200,
    "Pencils": 300,
    "Erasers": 400,
}

# Function to display current inventory
def display_inventory():
    message = "Current Inventory:\n\n"
    for item, qty in supplies.items():
        message += f"{item}: {qty}\n"
    messagebox.showinfo("Inventory", message)

# Function to display order window
def order_window():
    def submit_order():
        for item, qty in order_entries.items():
            supplies[item] += int(qty.get())
        messagebox.showinfo("Order Submitted", "The order has been submitted.")
        root.destroy()

    root = tk.Toplevel()
    root.title("Order Form")

    order_entries = {}
    for item in supplies.keys():
        label = tk.Label(root, text=item)
        label.pack()
        entry = tk.Entry(root)
        entry.pack()
        order_entries[item] = entry

    submit_button = tk.Button(root, text="Submit Order", command=submit_order)
    submit_button.pack()

# Function to generate inventory report
def generate_report():
    report = "Inventory Report\n\n"
    for item, qty in supplies.items():
        report += f"{item}: {qty}\n"
    with open("inventory_report.txt", "w") as f:
        f.write(report)
    messagebox.showinfo("Report Generated", "The inventory report has been generated.")

# Main window
root = tk.Tk()
root.title("School Inventory System")

# Add buttons and labels
display_button = tk.Button(root, text="Display Inventory", command=display_inventory)
display_button.pack()

order_button = tk.Button(root, text="Order Supplies", command=order_window)
order_button.pack()

report_button = tk.Button(root, text="Generate Report", command=generate_report)
report_button.pack()

root.mainloop()