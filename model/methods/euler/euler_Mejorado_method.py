import sympy as sp
from model.methods.base_method import BaseMethod

class EulerMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, xf)
        
    def step(self, x, y):
        y_pred = y + self.h * self.f(x, y)
        xnext = x + self.h
        return y + 0.5 * self.h * (self.f(x, y) + self.f(xnext, y_pred))