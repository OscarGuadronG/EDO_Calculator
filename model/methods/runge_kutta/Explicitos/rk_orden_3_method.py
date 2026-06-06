import sympy as sp
from model.methods.base_method import BaseMethod

class RK3Method(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, xf)
        
    def step(self, x, y):
        k1 = self.f(x, y)
        k2 = self.f(x + 0.5 * self.h, y + 0.5 * self.h * k1)
        k3 = self.f(x + self.h, y - self.h * k1 + 2.0 * self.h * k2)
        y_next = y + (self.h / 6.0) * (k1 + 4.0 * k2 + k3)
        return y_next