import customtkinter as ctk
from tkinter import ttk

class ResultTable(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnas = ["i", "x", "y"]
        self.tree = ttk.Treeview(self, columns=self.columnas, show="headings")

        for col in self.columnas:
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True)

    def load_data(self, data):
        
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, (x, y) in enumerate(data):
            self.tree.insert("", "end", values=(i, x, y))

