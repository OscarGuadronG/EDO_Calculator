import customtkinter as ctk

from controller.euler_controller import EulerController
from controller.main_controller import MainController
from view.components.left_sidebar import LeftSidebar
from view.frames.result_table import ResultTable
from view.frames.graph_result import GraphFrame


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
        # UI
        self.init_ui()
        # Cierre de la aplicación
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

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
        # X0
        row_x0 = ctk.CTkFrame(self.content)
        row_x0.pack(pady=5, padx=20, fill="x")
        row_x0.columnconfigure(1, weight=1)
        self.label_x0 = ctk.CTkLabel(row_x0, text="X0: ")
        self.label_x0.pack(side="left")
        self.entry_x0 = ctk.CTkEntry(row_x0, validate="key", validatecommand=vcmd_f)
        self.entry_x0.pack(side="left", padx=15)
        # Y0
        row_y0 = ctk.CTkFrame(self.content)
        row_y0.pack(pady=5, padx=20, fill="x")
        row_y0.columnconfigure(1, weight=1)
        self.label_y0 = ctk.CTkLabel(row_y0, text="Y0: ")
        self.label_y0.pack(side="left")
        self.entry_y0 = ctk.CTkEntry(row_y0, validate="key", validatecommand=vcmd_f)
        self.entry_y0.pack(side="left", padx=15)
        # h
        row_h = ctk.CTkFrame(self.content)
        row_h.pack(pady=5, padx=20, fill="x")
        row_h.columnconfigure(1, weight=1)
        self.label_h = ctk.CTkLabel(row_h, text="h:  ")
        self.label_h.pack(side="left")
        self.entry_h = ctk.CTkEntry(row_h, validate="key", validatecommand=vcmd_f)
        self.entry_h.pack(side="left", padx=15)
        ### Validación para N
        vcmd_i = (self.register(self.validate_int), '%P')
        row_n = ctk.CTkFrame(self.content)
        row_n.pack(pady=5, padx=20, fill="x")
        row_n.columnconfigure(1, weight=1)
        self.label_n = ctk.CTkLabel(row_n, text="N:  ")
        self.label_n.pack(side="left")
        self.entry_n = ctk.CTkEntry(row_n, validate="key", validatecommand=vcmd_i)
        self.entry_n.pack(side="left", padx=15)
        ### Boton de ejecucion y mensaje de error
        self.execute_button = ctk.CTkButton(self.content, text="Ejecutar",
                                            command=self.on_execute)
        self.execute_button.pack(pady=8, padx=20, fill="x")
        self.error_label = ctk.CTkLabel(self.content, text="", text_color="red")
        self.error_label.pack(pady=5, padx=20, fill="x")
        ## Tabla de resultados
        self.table = ResultTable(self.content)
        self.table.pack(fill="both", expand=True)
        self.btn_plot = ctk.CTkButton(self.content, text="Graficar", 
                                      state="disabled", command=self.on_plot)
        self.btn_plot.pack(pady=10, padx=20, fill="x")
        ## Frame para la gráfica
        self.graph_frame = GraphFrame(self.content)
        self.graph_frame.pack(fill="both", expand=True)
    
    ## Callbacks    
    def on_menu_select(self, selection):
        group, method = selection
        self.selected_group = group
        self.selected_method = method

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
            self.table.load_data(result["points"])
            self.btn_plot.configure(state="normal")
            self.current_result = result

        except ValueError as e:
            self.error_label.configure(text=str(e))

    def on_plot(self):
        x = self.current_result ["x"]
        y = self.current_result ["y"]
        ##Grafica
        self.graph_frame.plot(x, y)
        

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
    
    ##Cierre de la aplicación
    def on_closing(self):
        import matplotlib.pyplot as plt
        plt.close('all')
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()