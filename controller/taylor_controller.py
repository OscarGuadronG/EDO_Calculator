from model.methods.taylor.taylor_method import TaylorSecondOrderAutoMethod


class TaylorController:

    def execute(self, method, f, x0, y0, h, n):

        if method == "serie":

            solver = TaylorSecondOrderAutoMethod(
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