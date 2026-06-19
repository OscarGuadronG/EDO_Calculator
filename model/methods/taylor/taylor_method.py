import sympy as sp
from model.methods.base_method import BaseMethod

class TaylorSecondOrderAutoMethod(BaseMethod):
    def __init__(self, f_expr, x0, y0, h, n):
        """
        f_expr: Una cadena de texto con la función o una expresión de SymPy.
                Ejemplo: "x + y"
        """
        # Definimos las variables simbólicas
        self.x_sym = sp.Symbol('x')
        self.y_sym = sp.Symbol('y')
        
        # Convertimos el string a una expresión matemática de SymPy
        self.f_expr = sp.sympify(f_expr)
        
        # 1. Calculamos la derivada total automáticamente:
        # d/dx (f(x,y)) = df/dx + df/dy * dy/dx  (donde dy/dx es la misma f)
        df_dx = sp.diff(self.f_expr, self.x_sym)
        df_dy = sp.diff(self.f_expr, self.y_sym)
        self.df_expr = df_dx + df_dy * self.f_expr
        
        # 2. Convertimos las expresiones de SymPy en funciones de Python ultrarrápidas (lambdas)
        f_lambda = sp.lambdify((self.x_sym, self.y_sym), self.f_expr, 'numpy')
        self.df_lambda = sp.lambdify((self.x_sym, self.y_sym), self.df_expr, 'numpy')
        
        # Pasamos la función f_lambda a la clase base
        super().__init__(f_lambda, x0, y0, h, n)
    
    def step(self, x, y):
        # Evaluamos usando las funciones generadas automáticamente
        primer_orden = self.h * self.f(x, y)
        segundo_orden = ((self.h ** 2) / 2.0) * self.df_lambda(x, y)
        
        return y + primer_orden + segundo_orden