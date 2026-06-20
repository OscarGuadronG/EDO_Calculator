import sympy as sp
from model.methods.base_method import BaseMethod

class PredictorCorrectorMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, xf)
        
    def solve(self):
        results = [(self.x0, self.y0)]
        steps = int(round((self.xf - self.x0) / self.h))
        
        if steps < 1:
            return results
        # --- (BOOTSTRAP) CON RK4 ---
        # Necesitamos calcular (x1, y1), (x2, y2) y (x3, y3) para juntar los 4 puntos iniciales
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
        for n in range(3, steps):
            x_n, y_n = results[n]
            x_nm1, y_nm1 = results[n - 1]
            x_nm2, y_nm2 = results[n - 2]
            x_nm3, y_nm3 = results[n - 3]

            f_n = self.f(x_n, y_n)
            f_nm1 = self.f(x_nm1, y_nm1)
            f_nm2 = self.f(x_nm2, y_nm2)
            f_nm3 = self.f(x_nm3, y_nm3)
            x_next = x_n + self.h
        # Predictor (Adams-Bashforth 4)
            y_pred = y_n + (self.h / 24.0) * (
                55.0 * f_n - 59.0 * f_nm1
                + 37.0 * f_nm2 - 9.0 * f_nm3
            )

            f_pred = self.f(x_next, y_pred)

        # Corrector (Adams-Moulton 4)
            y_corr = y_n + (self.h / 24.0) * (
                9.0 * f_pred + 19.0 * f_n - 5.0 * f_nm1 + f_nm2 )

            results.append((x_next, y_corr))
            
        return results

    def step(self, x, y):
        pass