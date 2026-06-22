import sympy as sp
from model.methods.base_method import BaseMethod

class RK2Method(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, n, xf)
        
    def step(self, x, y):
        # Pendiente al inicio del intervalo
        k1 = self.f(x, y)
        
        # Pendiente calculada al final del intervalo aproximado
        k2 = self.f(x + self.h, y + self.h * k1)
        
        # El salto definitivo usando el promedio de ambas pendientes
        y_next = y + (self.h / 2.0) * (k1 + k2)
        return y_next