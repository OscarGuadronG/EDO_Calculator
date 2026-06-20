import sympy as sp
from model.methods.base_method import BaseMethod

class AdamsMoulton2Method(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, n)
        
    def solve(self):
        results = [(self.x0, self.y0)]
        steps = int(round((self.xf - self.x0) / self.h))
        
        if steps < 1:
            return results

        # --- ARRANQUE AUTOMÁTICO (BOOTSTRAP) CON RK4 ---
        # AM2 solo necesita 2 puntos históricos para iniciar, calculamos (x1, y1)
        x_curr, y_curr = results[0]
        k1 = self.f(x_curr, y_curr)
        k2 = self.f(x_curr + 0.5 * self.h, y_curr + 0.5 * self.h * k1)
        k3 = self.f(x_curr + 0.5 * self.h, y_curr + 0.5 * self.h * k2)
        k4 = self.f(x_curr + self.h, y_curr + self.h * k3)
        
        y_rk4 = y_curr + (self.h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x_rk4 = x_curr + self.h
        results.append((x_rk4, y_rk4))

        # --- CICLO PRINCIPAL PREDICTOR-CORRECTOR (AM2) ---
        # Ya tenemos los índices 0 y 1. Empezamos en n=1 para predecir el índice 2
        for n in range(1, steps):
            x_n, y_n = results[n]          # Punto actual (1 paso atrás)
            x_prev, y_prev = results[n-1]  # Punto anterior (2 pasos atrás)
            
            f_n = self.f(x_n, y_n)
            f_prev = self.f(x_prev, y_prev)
            
            x_next = x_n + self.h
            
            # --- PASO 1: PREDICCIÓN (Usando AB2) ---
            y_pred = y_n + (self.h / 2.0) * (3.0 * f_n - f_prev)
            
            # Pendiente en el punto futuro estimado
            f_next_pred = self.f(x_next, y_pred)
            
            # --- PASO 2: CORRECCIÓN (Usando la fórmula implícita AM2) ---
            # Coeficientes: (5*f_next + 8*f_n - f_prev) / 12
            y_next = y_n + (self.h / 12.0) * (5.0 * f_next_pred + 8.0 * f_n - f_prev)
            
            results.append((x_next, y_next))
            
        return results

    def step(self, x, y):
        pass