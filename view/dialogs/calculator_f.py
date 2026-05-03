import customtkinter as ctk
from sympy import sympify, symbols, lambdify

x, y = symbols('x y')

class CalculatorF(ctk.CTkToplevel):
    def __init__(self, master, callback):
        super().__init__(master)

        self.callback = callback
        self.title("Ingresar función f(x, y)")
        self.geometry("400x300")

        self.entry = ctk.CTkEntry(self, width=300)
        self.entry.pack(pady=10)
        self.label_info = ctk.CTkLabel(self, text="Ej: x + y**2 | sin(x) + y | sqrt(x)")
        self.label_info.pack()
        # Frames para organizar botones
        frame_trig = ctk.CTkFrame(self)
        frame_trig.pack(pady=5)

        botones = [ ("sin", "sin("), ("cos", "cos("), ("tan", "tan("),
                    ("sin⁻¹", "asin("), ("cos⁻¹", "acos("), ("tan⁻¹", "atan("),
                    ("√", "sqrt("), ("ln", "log(") ]
        for i, (text, val) in enumerate(botones):
            btn = ctk.CTkButton(frame_trig, text=text, command=lambda v=val: self.insert(v))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
        self.button = ctk.CTkButton(self, text="Aceptar", command=self.aceptar)
        self.button.pack(pady=10)

    def normalizar(self, expr):
        # Reemplazar potencias con ** y funciones con su sintaxis de sympy
        reemplazos = {
            '^': '**',
            'sin': 'sin',
            'cos': 'cos',
            'tan': 'tan',
            'sqrt': 'sqrt',
            'ln': 'log'
        }
        for key, val in reemplazos.items():
            expr = expr.replace(key, val)
        return expr
    
    def insert(self, text):
        self.entry.insert("insert", text)
        self.entry.focus()

    def aceptar(self):
        expr_str = self.entry.get()
        expr_str = self.normalizar(expr_str)
        try:
            expresion = sympify(expr_str)
            if not expresion.free_symbols.issubset({x, y}):
                raise ValueError
            f = lambdify((x, y), expresion, "numpy")
            self.callback(f, expr_str)
            self.destroy()
        except Exception as e:
            self.label_info.configure(text="Expresión inválida")
    
