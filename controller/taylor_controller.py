from model.methods.taylor.taylor_method import TaylorMethod

class TaylorController:
    def execute(self, method, f, x0, y0, h, xf, **keywargs):
        order = keywargs.get("order")
        if method == "serie":
            solver = TaylorMethod(f, x0, y0, h, xf, order)
        else:
            raise ValueError(f"Método '{method}' no soportado en TaylorController")
        return solver.solve()