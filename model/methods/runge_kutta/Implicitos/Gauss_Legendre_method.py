import numpy as np
import sympy as sp
from scipy.optimize import fsolve
from model.methods.base_method import BaseMethod

class GaussLegendreMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, n)
        
        # Constantes del método de Gauss-Legendre de 2 puntos
        self.c1 = 0.5 - np.sqrt(3)/6
        self.c2 = 0.5 + np.sqrt(3)/6
        
        self.a11 = 0.25
        self.a12 = 0.25 - np.sqrt(3)/6
        self.a21 = 0.25 + np.sqrt(3)/6
        self.a22 = 0.25

    def step(self, x, y):
        x1 = x + self.c1 * self.h
        x2 = x + self.c2 * self.h

        # Sistema de 2 ecuaciones acopladas para k1 y k2
        def sistema_k(ks):
            k1, k2 = ks
            eq1 = k1 - self.f(x1, y + self.h * (self.a11 * k1 + self.a12 * k2))
            eq2 = k2 - self.f(x2, y + self.h * (self.a21 * k1 + self.a22 * k2))
            return [eq1, eq2]

        # Predicción inicial aproximando k1 y k2 con la pendiente al inicio
        k_inicial = self.f(x, y)
        prediccion_inicial = [k_inicial, k_inicial]

        # fsolve resuelve el sistema vectorial
        k1_opt, k2_opt = fsolve(sistema_k, prediccion_inicial)

        # Avance final usando pesos b1 = 0.5 y b2 = 0.5
        return y + (self.h / 2.0) * (k1_opt + k2_opt)