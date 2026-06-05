from model.methods.euler.euler_method import EulerMethod


def f(x, y):
    return x + y

def test_euler_method():
    x0 = 0
    y0 = 1
    h = 0.1
    xf = 0.5
    f_expr = "2*x*y"
    method = EulerMethod(f_expr, x0, y0, h, xf)
    results = method.solve()

    print(f"\nValores calculados por tu EulerMethod para f(x,y) = {f_expr}:")
    print("--------------------------------------------------")
    print(f"{'Punto':<8}{'x':<12}{'y aproximado':<15}")
    print("--------------------------------------------------")
    for idx, r in enumerate(results):
        print(f"{idx+1:<8}{round(r[0], 2):<12}{round(r[1], 8):<15}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    test_euler_method()
    print("¡Ejecución de Euler completada con éxito!")