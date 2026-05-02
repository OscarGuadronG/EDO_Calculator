import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.figure = None
        self.canvas = None

    def plot(self, x, y):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        ##Grafica
        self.figure, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.set_title(f"Grafica de resultados")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ## Integración con Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
