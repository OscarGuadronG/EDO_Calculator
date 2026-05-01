import customtkinter as ctk
from view.components.left_sidebar import LeftSidebar
class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("EDO Calculator")
        self.geometry("900x500")

        self.init_ui()

    def init_ui(self):
        # Sidebar
        self.sidebar = LeftSidebar(self, self.on_menu_select)
        self.sidebar.pack(side="left", fill="y")

        # Área principal (vacía por ahora)
        self.content = ctk.CTkFrame(self)
        self.content.pack(side="right", expand=True, fill="both")

    def on_menu_select(self, selection):
        group, method = selection
        print("Seleccionado:", group, method)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()