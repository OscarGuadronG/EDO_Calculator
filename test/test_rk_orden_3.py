from model.methods.runge_kutta.Explicitos.rk_orden_3_method import RK3Method

def test_rk3_specific():

    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 5
    f_expr = "2*x*y"


    method = RK3Method(f_expr, x0, y0, h, xf)
    results = method.solve()

    print(f"\nValores calculados por RK3 para f(x,y) = {f_expr}:")
    print("--------------------------------------------------")
    print(f"{'Punto':<8}{'x':<12}{'y aproximado':<15}")
    print("--------------------------------------------------")
    for idx, r in enumerate(results):
        print(f"{idx+1:<8}{round(r[0], 2):<12}{round(r[1], 8):<15}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    test_rk3_specific()