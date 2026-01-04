import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x450")
root.resizable(False, False)

tasks = []

# Functions
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task")

def clear_tasks():
    listbox.delete(0, tk.END)
    tasks.clear()

# Title
title = tk.Label(root, text="📝 TO-DO LIST", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

# Buttons
btn_add = tk.Button(root, text="Add Task", width=20, command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Task", width=20, command=delete_task)
btn_delete.pack(pady=5)

btn_clear = tk.Button(root, text="Clear All", width=20, command=clear_tasks)
btn_clear.pack(pady=5)

# Task list
listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=10)
listbox.pack(pady=15)

# Run app
root.mainloop()
