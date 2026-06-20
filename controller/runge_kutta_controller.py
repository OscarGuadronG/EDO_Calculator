from model.methods.runge_kutta.Explicitos.ralston_method import RalstonMethod
from model.methods.runge_kutta.Explicitos.punto_medio import RK2MidpointMethod
from model.methods.runge_kutta.Explicitos.rk_orden_2_method import RK2Method
from model.methods.runge_kutta.Explicitos.rk_orden_3_method import RK3Method
from model.methods.runge_kutta.Explicitos.rk_orden_4_method import RK4Method
from model.methods.runge_kutta.Implicitos.Gauss_Legendre_method import GaussLegendreMethod
from model.methods.runge_kutta.Implicitos.traprecio_method import TrapecioMethod

class RungeKuttaController:

    def execute(self, method, f, x0, y0, h, n):

        if method == "punto_medio":
            solver = RK2MidpointMethod(f,x0,y0,h,n)

        elif method == "ralston":
            solver = RalstonMethod(f,x0,y0,h,n)

        elif method == "rk2":
            solver = RK2Method(f,x0,y0,h,n)

        elif method == "rk3":
            solver = RK3Method(f,x0,y0,h,n)

        elif method == "rk4":
            solver = RK4Method(f,x0,y0,h,n)

        elif method == "gauss_legendre":
            solver = GaussLegendreMethod(f,x0,y0,h,n)

        elif method == "trapecio":
            solver = TrapecioMethod(f,x0,y0,h,n)
            
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