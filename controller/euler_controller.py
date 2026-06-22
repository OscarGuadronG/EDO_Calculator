from model.methods.euler.euler_method import EulerMethod
from model.methods.euler.euler_Mejorado_method import EulerMejorado
from model.methods.euler.euler_implicito import EulerImplicito

class EulerController:

    def execute(self, method, f, x0, y0, h, n, xf, **keywargs):
        if method == "explicito":
            solver = EulerMethod(f, x0, y0, h, n, xf)
        elif method == "mejorado":
            solver = EulerMejorado(f, x0, y0, h, n, xf)
        elif method == "implicito":
            solver = EulerImplicito(f, x0, y0, h, n, xf)
        else:
            raise ValueError(
                f"Método '{method}' no soportado"
            )

        results = solver.solve()

        return {
                "points": results,
                "x": [p[0] for p in results],
                "y": [p[1] for p in results],
            }
    
