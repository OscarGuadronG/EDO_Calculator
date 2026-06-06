import sympy as sp
from model.methods.base_method import BaseMethod

class EulerMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf):
        """
        f_expr: Una cadena de texto con la función (ej. "2*x*y" o "(x**2 + 1)/y")
        """
        # 1. Definimos las variables simbólicas obligatorias para SymPy
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        
        # 2. Convertimos el string a una expresión matemática de SymPy
        self.f_expr = sp.sympify(f_expr)
        
        # 3. Convertimos la expresión de SymPy en una función lambda de Python
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        
        # 4. Le pasamos esa función lambda ya lista a la clase base
        super().__init__(f_lambda, x0, y0, h, xf)
        
    def step(self, x, y):
        # El método step queda super limpio y corto, justo como lo tenías
        return y + self.h * self.f(x, y)