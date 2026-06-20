import sympy as sp
from model.methods.base_method import BaseMethod

class RalstonMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, n)
        
    def step(self, x, y):
        k1 = self.f(x, y)
        x_ralston = x + 0.75 * self.h
        y_ralston = y + 0.75 * self.h * k1
        k2 = self.f(x_ralston, y_ralston)
        
        # Combinación lineal óptima de Ralston
        return y + self.h * ((1/3) * k1 + (2/3) * k2)