import sympy as sp
from model.methods.base_method import BaseMethod

class RK2MidpointMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, xf)
        
    def step(self, x, y):
        k1 = self.f(x, y)
        x_half = x + 0.5 * self.h
        y_half = y + 0.5 * self.h * k1
        k2 = self.f(x_half, y_half)
        return y + self.h * k2