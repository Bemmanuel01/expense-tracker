import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        expenses.append({'amount': amount, 'category': category})
        messagebox.showinfo("Success", f"Added {amount} under '{category}'")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def list_expenses():
    output_text.delete('1.0', tk.END)
    for exp in expenses:
        output_text.insert(tk.END, f"Amount: {exp['amount']}, Category: {exp['category']}\n")

def show_total():
    total = sum(exp['amount'] for exp in expenses)
    messagebox.showinfo("Total Expenses", f"Total: {total}")

def filter_by_category():
    cat = filter_entry.get()
    filtered = filter(lambda e: e['category'] == cat, expenses)
    output_text.delete('1.0', tk.END)
    for exp in filtered:
        output_text.insert(tk.END, f"Amount: {exp['amount']}, Category: {exp['category']}\n")

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=2, columnspan=2, pady=5)

tk.Button(root, text="List Expenses", command=list_expenses).grid(row=3, column=0)
tk.Button(root, text="Show Total", command=show_total).grid(row=3, column=1)

tk.Label(root, text="Filter by Category").grid(row=4, column=0)
filter_entry = tk.Entry(root)
filter_entry.grid(row=4, column=1)

tk.Button(root, text="Filter", command=filter_by_category).grid(row=5, columnspan=2, pady=5)

output_text = tk.Text(root, height=10, width=40)
output_text.grid(row=6, columnspan=2, pady=10)

root.mainloop()