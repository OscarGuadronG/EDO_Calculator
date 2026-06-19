from model.methods.euler.euler_method import EulerMethod
from model.methods.euler.euler_Mejorado_method import EulerMejoradoMethod
from model.methods.euler.euler_implicito import Euler_Implicit_Method


class EulerController:

    def execute(self, method, f, x0, y0, h, n):

        if method == "explicito":
            solver = EulerMethod(
                f,
                x0,
                y0,
                h,
                n
            )

        elif method == "mejorado":
            solver = EulerMejoradoMethod(
                f,
                x0,
                y0,
                h,
                n
            )

        elif method == "implicito":
            solver = Euler_Implicit_Method(
                f,
                x0,
                y0,
                h,
                n
            )

        else:
            raise ValueError(
                f"Método '{method}' no soportado"
            )

        results = solver.solve()

        return {
            "points": results,
            "x": [p[0] for p in results],
            "y": [p[1] for p in results],
            "xf": solver.xf,
        }