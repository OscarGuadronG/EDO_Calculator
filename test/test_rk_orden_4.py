from model.methods.runge_kutta.Explicitos.rk_orden_4_method import RK4Method

def test_rk4_specific():

    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 5
    f_expr = "2*x*y"


    method = RK4Method(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nNuevos valores calculados por RK4:")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 8)}),")


if __name__ == "__main__":
    test_rk4_specific()
    print("¡All tests passed!")