import sympy as sp
from model.methods.base_method import BaseMethod

class AdamsMoulton3Method(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, n, xf)
        
    def solve(self):
        results = [(self.x0, self.y0)]
        steps = int(round((self.xf - self.x0) / self.h))
        
        if steps < 1:
            return results

        # --- ARRANQUE AUTOMÁTICO (BOOTSTRAP) CON RK4 ---
        # AM3 necesita 3 puntos iniciales en total para arrancar: (x0, y0), (x1, y1), (x2, y2)
        for i in range(2):
            if len(results) - 1 >= steps:
                break
            x_curr, y_curr = results[-1]
            
            k1 = self.f(x_curr, y_curr)
            k2 = self.f(x_curr + 0.5 * self.h, y_curr + 0.5 * self.h * k1)
            k3 = self.f(x_curr + 0.5 * self.h, y_curr + 0.5 * self.h * k2)
            k4 = self.f(x_curr + self.h, y_curr + self.h * k3)
            
            y_rk4 = y_curr + (self.h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
            x_rk4 = x_curr + self.h
            results.append((x_rk4, y_rk4))

        # --- CICLO PRINCIPAL PREDICTOR-CORRECTOR (AM3) ---
        # Empezamos en n=2 para predecir el índice 3 usando la historia previa
        for n in range(2, steps):
            x_n, y_n = results[n]          # 1 paso atrás (actual)
            x_prev1, y_prev1 = results[n-1]  # 2 pasos atrás
            x_prev2, y_prev2 = results[n-2]  # 3 pasos atrás
            
            f_n = self.f(x_n, y_n)
            f_prev1 = self.f(x_prev1, y_prev1)
            f_prev2 = self.f(x_prev2, y_prev2)
            
            x_next = x_n + self.h
            
            # --- PASO 1: PREDICCIÓN (Fórmula de AB3) ---
            y_pred = y_n + (self.h / 12.0) * (23.0 * f_n - 16.0 * f_prev1 + 5.0 * f_prev2)
            
            # Pendiente en el punto futuro estimado
            f_next_pred = self.f(x_next, y_pred)
            
            # --- PASO 2: CORRECCIÓN (Fórmula implícita AM3) ---
            # Coeficientes exactos: (9*f_next + 19*f_n - 5*f_prev1 + f_prev2) / 24
            y_next = y_n + (self.h / 24.0) * (9.0 * f_next_pred + 19.0 * f_n - 5.0 * f_prev1 + f_prev2)
            
            results.append((x_next, y_next))
            
        return results

    def step(self, x, y):
        pass