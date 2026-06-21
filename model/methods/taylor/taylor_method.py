import sympy as sp
from model.methods.base_method import BaseMethod

class TaylorMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf, order):
        print("Antes de construir Taylor")
        self.order = order
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        
        # Convertimos el string a una expresión matemática de SymPy
        self.f_expr = sp.sympify(f_expr)
        self.derivadas = []
        self.derivadas.append(self.f_expr)

        # 1. Calculamos las derivadas necesarias para la serie de Taylor
        current = self.f_expr

        for i in range(order - 1):
            current = self.derivada_total(current)
            self.derivadas.append(current)
        
        taylor_expr = self.y_sym
            
        for i, derivada in enumerate(self.derivadas):
            taylor_expr += (h ** (i + 1)) * derivada / sp.factorial(i + 1)
        
        # Creamos una función lambda a partir de la expresión de Taylor
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), taylor_expr, "numpy")
        print("Taylor construido")
        # Pasamos la función f_lambda a la clase base
        super().__init__(f_lambda, x0, y0, h, xf)
    
    def step(self, x, y):
        return self.f(x, y)

    def derivada_total(self, expr):
        dx = sp.diff(expr, self.x_sym)
        dy = sp.diff(expr, self.y_sym)

        return dx + dy * self.f_expr