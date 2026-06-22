import sympy as sp
from scipy.optimize import fsolve
from model.methods.base_method import BaseMethod

class TrapecioMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, n, xf)
        
    def step(self, x, y):
        xnext = x + self.h
        pendiente_inicial = self.f(x, y)
        
        # Definimos la ecuación del trapecio: y_next - y - (h/2)*(f(x,y) + f(x_next, y_next)) = 0
        def ecuacion_trapecio(y_futuro):
            return y_futuro - y - (self.h / 2.0) * (pendiente_inicial + self.f(xnext, y_futuro))
        
        prediccion_inicial = y + self.h * pendiente_inicial
        
        y_next = fsolve(ecuacion_trapecio, prediccion_inicial)[0]
        
        return y_next