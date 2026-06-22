import sympy as sp
from model.methods.base_method import BaseMethod

class AdamsMoulton4Method(BaseMethod):
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
        # AM4 requiere 4 puntos históricos iniciales: índices 0, 1, 2 y 3
        for i in range(3):
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

        # --- CICLO PRINCIPAL PREDICTOR-CORRECTOR (AM4) ---
        # Empezamos en n=3 para calcular el punto futuro (índice 4)
        for n in range(3, steps):
            x_n, y_n = results[n]          # 1 paso atrás (actual)
            x_prev1, y_prev1 = results[n-1]  # 2 pasos atrás
            x_prev2, y_prev2 = results[n-2]  # 3 pasos atrás
            x_prev3, y_prev3 = results[n-3]  # 4 pasos atrás
            
            f_n = self.f(x_n, y_n)
            f_prev1 = self.f(x_prev1, y_prev1)
            f_prev2 = self.f(x_prev2, y_prev2)
            f_prev3 = self.f(x_prev3, y_prev3)
            
            x_next = x_n + self.h
            
            # --- PASO 1: PREDICCIÓN (Fórmula de AB4) ---
            y_pred = y_n + (self.h / 24.0) * (55.0 * f_n - 59.0 * f_prev1 + 37.0 * f_prev2 - 9.0 * f_prev3)
            
            # Pendiente en el punto futuro estimado
            f_next_pred = self.f(x_next, y_pred)
            
            # --- PASO 2: CORRECCIÓN (Fórmula implícita AM4) ---
            # Coeficientes exactos sobre 720: (251*f_next + 646*f_n - 264*f_prev1 + 106*f_prev2 - 19*f_prev3)
            y_next = y_n + (self.h / 720.0) * (
                251.0 * f_next_pred + 646.0 * f_n - 264.0 * f_prev1 + 106.0 * f_prev2 - 19.0 * f_prev3
            )
            
            results.append((x_next, y_next))
            
        return results

    def step(self, x, y):
        pass