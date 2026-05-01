import customtkinter as ctk
from view.style import theme
from view.components.create_seccion import CreateSeccion

class LeftSidebar(ctk.CTkFrame):
    
    def __init__(self, master, on_select):
        super().__init__(master)
        self.on_select = on_select
        self.build()
    
    def build(self):
        euler_seccion = CreateSeccion(self, "Euler", [
            ("Explícito", ("euler", "explicito")),
            ("Mejorado", ("euler", "mejorado")),
        ], self.on_select)
        euler_seccion.pack(fill="x")
    