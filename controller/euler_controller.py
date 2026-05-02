from model.methods.euler.euler_method import EulerMethod

class EulerController:

    def execute(self, method, f, x0, y0, h, n):
        if method == "explicito":
            solver = EulerMethod(f, x0, y0, h, n)
        else:
            raise ValueError("Metodo no soportado")
        results = solver.solve()
        return {
                "points": results,
                "x": [p[0] for p in results],
                "y": [p[1] for p in results],
                "xf": solver.xf,
            }
    