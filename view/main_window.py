import customtkinter as ctk
from controller.euler_controller import EulerController
from controller.main_controller import MainController
from view.components.left_sidebar import LeftSidebar

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("EDO Calculator")
        self.geometry("900x500")
        # Estado inicial
        self.selected_group = 'euler'
        self.selected_method = 'explicito'
        # Controladores
        controllers = {
            'euler': EulerController()
        }
        self.main_controller = MainController(controllers)

        self.init_ui()

    def init_ui(self):
        # Sidebar
        self.sidebar = LeftSidebar(self, self.on_menu_select)
        self.sidebar.pack(side="left", fill="y")

        # Area de contenido
        self.content = ctk.CTkFrame(self)
        self.content.pack(side="right", expand=True, fill="both")
        ## Entradas
        ### Validación para floats
        vcmd_f = (self.register(self.validate_float), '%P')
        self.entry_x0 = ctk.CTkEntry(self.content, placeholder_text="X0",
                                        validate="key", validatecommand=vcmd_f)
        self.entry_x0.pack(pady=10, padx=20, fill="x")
        self.entry_y0 = ctk.CTkEntry(self.content, placeholder_text="Y0",
                                        validate="key", validatecommand=vcmd_f)
        self.entry_y0.pack(pady=10, padx=20, fill="x")
        self.entry_h = ctk.CTkEntry(self.content, placeholder_text="h",
                                        validate="key", validatecommand=vcmd_f)
        self.entry_h.pack(pady=10, padx=20, fill="x")
        ### Validación para N
        vcmd_i = (self.register(self.validate_int), '%P')
        self.entry_n = ctk.CTkEntry(self.content, placeholder_text="N",
                                        validate="key", validatecommand=vcmd_i)
        self.entry_n.pack(pady=10, padx=20, fill="x")
        ### Boton de ejecucion y mensaje de error
        self.execute_button = ctk.CTkButton(self.content, text="Ejecutar",
                                            command=self.on_execute)
        self.execute_button.pack(pady=10, padx=20, fill="x")
        self.error_label = ctk.CTkLabel(self.content, text="", text_color="red")
        self.error_label.pack(pady=5, padx=20, fill="x")
    
    ## Callbacks    
    def on_menu_select(self, selection):
        group, method = selection
        self.selected_group = group
        self.selected_method = method
        print(f"Seleccionado: Grupo={group}, Método={method}")

    def on_execute(self):
        try:
            
            x0 = float(self.entry_x0.get())
            y0 = float(self.entry_y0.get())
            h = float(self.entry_h.get())
            if h <= 0:
                raise ValueError("h debe ser positivo mayor a 0")
                return
            steps = int(self.entry_n.get())
            if steps < 2:
                raise ValueError("N debe ser mayor o igual a 2")
                return
            self.error_label.configure(text="")
            # Función de prueba
            f = lambda x, y: x + y
            result = self.main_controller.execute_group(
                self.selected_group,
                self.selected_method,
                f, x0, y0, h, steps
            )
            print("Resultado:", result)
            self.error_label.configure(text="Ejecución exitosa", text_color="green")

        except ValueError as e:
            self.error_label.configure(text=str(e))

    ##Validaciones
    def validate_float(self, value):
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def validate_int(self, value):
        if value == "":
            return True
        
        return value.isdigit()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()