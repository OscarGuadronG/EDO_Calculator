import sympy as sp
from model.methods.base_method import BaseMethod

class AdamsBashforth2Method(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, xf):
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        self.f_expr = sp.sympify(f_expr)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        super().__init__(f_lambda, x0, y0, h, xf)
        
    def solve(self):
        # Inicializamos la lista de resultados con el punto inicial
        results = [(self.x0, self.y0)]
        
        # Si el intervalo es demasiado corto, terminamos temprano
        if self.x0 >= self.xf:
            return results
            
        # --- PASO DE ARRANQUE (BOOTSTRAP) ---
        # Como AB2 necesita el paso actual (n) y el anterior (n-1), 
        # usamos RK4 para calcular de forma segura el segundo punto (x1, y1).
        x0, y0 = self.x0, self.y0
        k1 = self.f(x0, y0)
        k2 = self.f(x0 + 0.5 * self.h, y0 + 0.5 * self.h * k1)
        k3 = self.f(x0 + 0.5 * self.h, y0 + 0.5 * self.h * k2)
        k4 = self.f(x0 + self.h, y0 + self.h * k3)
        y1 = y0 + (self.h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x1 = x0 + self.h
        
        results.append((x1, y1))
        
        # --- CICLO PRINCIPAL MULTIPASOS (AB2) ---
        # Empezamos a iterar desde el índice 1 para calcular el punto futuro (índice 2)
        steps = int(round((self.xf - self.x0) / self.h))
        
        for n in range(1, steps):
            x_n, y_n = results[n]          # Punto actual
            x_prev, y_prev = results[n-1]  # Punto anterior
            
            # Evaluamos las pendientes históricas
            f_n = self.f(x_n, y_n)
            f_prev = self.f(x_prev, y_prev)
            
            # Fórmula de Adams-Bashforth de 2 pasos
            y_next = y_n + (self.h / 2.0) * (3.0 * f_n - f_prev)
            x_next = x_n + self.h
            
            results.append((x_next, y_next))
            
        return results

    def step(self, x, y):
        # Sobrescribimos el método abstracto obligatorio de BaseMethod,
        # aunque AB2 controla su propia lógica secuencial en solve()
        pass