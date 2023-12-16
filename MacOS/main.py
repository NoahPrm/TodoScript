import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App by NoahPrm")

        self.load_tasks()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Ajouter Tâche", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Supprimer Tâche", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.update_listbox()

    def add_task(self):
        task = simpledialog.askstring("Ajouter Tâche", "Entrez la tâche:")
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.save_tasks()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_listbox()
            self.save_tasks()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        try:
            with open("./tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("./tasks.json", "w") as file:
            json.dump(self.tasks, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
