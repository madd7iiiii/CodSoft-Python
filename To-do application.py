import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.root.geometry("400x500")
        style = Style(theme="flatly")
        style.configure("custon.TEntry", forground="yellow")
        
        self.tasks = []

        self.load_tasks()

        
        self.create_widgets()
        self.task_entry.insert(0, "Enter your todo here...")

        self.task_entry.bind("<FocusIn>", self.clear_placeholder)

        self.task_entry.bind("<FocusOut>", self.restore_placeholder)

    def create_widgets(self):
        self.task_entry = ttk.Entry(self.root, font=("Brush Script MT", 16))
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)

        add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5, padx=10, fill=tk.X)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=("Helvetica", 12))

        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.update_task_listbox()

        delete_button = ttk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5, padx=10, fill=tk.X)

        complete_button = ttk.Button(self.root, text="Complete Task", command=self.complete_task)
        complete_button.pack(pady=5, padx=10, fill=tk.X)

        stats_button = ttk.Button(self.root, text="View Stats", command=self.view_stats)
        stats_button.pack(pady=5, padx=10, fill=tk.X)

    def add_task(self):

        task_text = self.task_entry.get().strip()
        if task_text:
            new_task = {"text": task_text, "created_at": str(datetime.now()), "completed": False}
            self.tasks.append(new_task)

            self.update_task_listbox()
            self.save_tasks()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):

        selected_index = self.task_listbox.curselection()
        if selected_index:

            del self.tasks[selected_index[0]]
            self.update_task_listbox()
            self.save_tasks()

    def clear_placeholder(self, event):
            if self.task_entry.get() == "Enter your todo here...":
                self.task_entry.delete(0, tk .END)

                self.task_entry.configure(style="TEntry")

    def restore_placeholder(self, event):
            if self.task_entry.get() == "":
                self.task_entry.insert(0, "Enter your todo here...")

                self.task_entry.configure(style="Custon.TEntry")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["completed"] = True

            self.update_task_listbox()
            self.save_tasks()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[✔] " if task["completed"] else "[✖] "

            self.task_listbox.insert(tk.END, f"{status}{task['text']}")

    def view_stats(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(task["completed"] for task in self.tasks)
        remaining_tasks = total_tasks - completed_tasks

        messagebox.showinfo("Task Stats", f"Total Tasks: {total_tasks}\nCompleted: {completed_tasks}\nRemaining: {remaining_tasks}")

    def save_tasks(self):
        with open("tasks.json", "w") as file:

            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:

                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
