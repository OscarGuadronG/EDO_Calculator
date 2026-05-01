class euler_controller:

    def __init__(self, model):
        self.model = model

    def execute(self, method, f, x0, y0, h, n):
        if method == "explicito":
            solver = self.model.euler_method(f, x0, y0, h, n)
        else:
            raise ValueError("Metodo no soportado")
        results = solver.solve()
        return {
                "points": results,
                "x": [p[0] for p in results],
                "y": [p[1] for p in results],
                "xf": solver.xf,
                "n": solver.n,
                "h": solver.h
            }