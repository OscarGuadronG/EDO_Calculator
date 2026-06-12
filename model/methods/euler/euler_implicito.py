import sympy as sp
from scipy.optimize import fsolve
from model.methods.base_method import BaseMethod

class EulerImplicito(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, xf)
        
    def step(self, x, y):
        xnext = x + self.h
        
        # Definimos la ecuación implícita: y_next - y - h * f(x_next, y_next) = 0
        def ecuacion_implicita(y_futuro):
            return y_futuro - y - self.h * self.f(xnext, y_futuro)
        
        # Usamos una predicción inicial (Euler simple) para ayudar a fsolve a converger rápido
        prediccion_inicial = y + self.h * self.f(x, y)
        
        # fsolve encuentra el valor exacto de y_next que hace la ecuación igual a 0
        y_next = fsolve(ecuacion_implicita, prediccion_inicial)[0]
        
        return y_next