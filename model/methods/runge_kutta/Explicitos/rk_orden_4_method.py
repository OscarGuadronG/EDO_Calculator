import sympy as sp
from model.methods.base_method import BaseMethod

class RK4Method(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, n)
        
    def step(self, x, y):
        k1 = self.f(x, y)
        
        x_half = x + 0.5 * self.h
        k2 = self.f(x_half, y + 0.5 * self.h * k1)
        k3 = self.f(x_half, y + 0.5 * self.h * k2)
        
        x_next = x + self.h
        k4 = self.f(x_next, y + self.h * k3)
        
        
        return y + (self.h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)