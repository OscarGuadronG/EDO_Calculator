from model.methods.multipasos.adams_bashfoth import adams_bashforth_2_method
from model.methods.multipasos.adams_bashfoth import adams_bashforth_3_method
from model.methods.multipasos.adams_bashfoth import adams_bashforth_4_method
from model.methods.multipasos.Adams_Moulton import adams_moulton_2_method
from model.methods.multipasos.Adams_Moulton import adams_moulton_3_method
from model.methods.multipasos.Adams_Moulton import adams_moulton_4_method

class MultipasosController:

    def execute(self, method, f, x0, y0, h, xf, **keywargs):
        if method == "bash_2":
            solver = adams_bashforth_2_method(f, x0, y0, h, xf)
        if method == "bash_3":
            solver = adams_bashforth_3_method(f, x0, y0, h, xf)
        if method == "bash_4":
            solver = adams_bashforth_4_method(f, x0, y0, h, xf)
        if method == "moulton_2":
            solver = adams_moulton_2_method(f, x0, y0, h, xf)
        if method == "moulton_3":
            solver = adams_moulton_3_method(f, x0, y0, h, xf)
        if method == "moulton_4":
            solver = adams_moulton_4_method(f, x0, y0, h, xf)
        else:
            raise ValueError("Metodo no soportado")
        results = solver.solve()
        return {
                "points": results,
                "x": [p[0] for p in results],
                "y": [p[1] for p in results],
            }