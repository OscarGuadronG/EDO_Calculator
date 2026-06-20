from model.methods.multipasos.adams_bashfoth import adams_bashforth_2_method
from model.methods.multipasos.adams_bashfoth import adams_bashforth_3_method
from model.methods.multipasos.adams_bashfoth import adams_bashforth_4_method
from model.methods.multipasos.Adams_Moulton import adams_moulton_2_method
from model.methods.multipasos.Adams_Moulton import adams_moulton_3_method
from model.methods.multipasos.Adams_Moulton import adams_moulton_4_method
from model.methods.multipasos.predictor_corrector import PredictorCorrectorMethod

class MultipasosController:

    def execute(self, method, f, x0, y0, h, xf, **keywargs):
        if method == "ab2":
            solver = adams_bashforth_2_method(f, x0, y0, h, xf)
        if method == "ab3":
            solver = adams_bashforth_3_method(f, x0, y0, h, xf)
        if method == "ab4":
            solver = adams_bashforth_4_method(f, x0, y0, h, xf)
        if method == "am2":
            solver = adams_moulton_2_method(f, x0, y0, h, xf)
        if method == "am3":
            solver = adams_moulton_3_method(f, x0, y0, h, xf)
        if method == "am4":
            solver = adams_moulton_4_method(f, x0, y0, h, xf)
        if method == "predictor_corrector":
            solver = PredictorCorrectorMethod(f, x0, y0, h, xf)
        else:
            raise ValueError(f"Método '{method}' no soportado")
        results = solver.solve()
        return {
                "points": results,
                "x": [p[0] for p in results],
                "y": [p[1] for p in results],
            }
