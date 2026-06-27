from model.methods.multipasos.adams_bashfoth.adams_bashforth_2_method import AdamsBashforth2Method
from model.methods.multipasos.adams_bashfoth.adams_bashforth_3_method import AdamsBashforth3Method
from model.methods.multipasos.adams_bashfoth.adams_bashforth_4_method import AdamsBashforth4Method
from model.methods.multipasos.Adams_Moulton.adams_moulton_2_method import AdamsMoulton2Method
from model.methods.multipasos.Adams_Moulton.adams_moulton_3_method import AdamsMoulton3Method
from model.methods.multipasos.Adams_Moulton.adams_moulton_4_method import AdamsMoulton4Method
from model.methods.multipasos.predictor_corrector import PredictorCorrectorMethod

class MultipasosController:

    def execute(self, method, f, x0, y0, h, n, xf, **keywargs):
        if method == "ab2":
            solver = AdamsBashforth2Method(f, x0, y0, h, n, xf)
        elif method == "ab3":
            solver = AdamsBashforth3Method(f, x0, y0, h, n, xf)
        elif method == "ab4":
            solver = AdamsBashforth4Method(f, x0, y0, h, n, xf)
        elif method == "am2":
            solver = AdamsMoulton2Method(f, x0, y0, h, n, xf)
        elif method == "am3":
            solver = AdamsMoulton3Method(f, x0, y0, h, n, xf)
        elif method == "am4":
            solver = AdamsMoulton4Method(f, x0, y0, h, n, xf)
        elif method == "predictor_corrector":
            solver = PredictorCorrectorMethod(f, x0, y0, h, n, xf)
        else:
            raise ValueError(f"Método '{method}' no soportado")
        results = solver.solve()
        return {
                "points": results,
                "x": [p[0] for p in results],
                "y": [p[1] for p in results],
            }
