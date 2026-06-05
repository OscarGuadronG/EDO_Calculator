from model.methods.runge_kutta.Explicitos.ralston_method import RalstonMethod

def test_ralston_specific():
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 1.2

    f_expr = "x + y"

    method = RalstonMethod(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nNuevos valores calculados por Ralston:")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 8)}),")

    # Valores teóricos calculados con el esquema de Ralston para x + y
    expected_results = [
        (0.0, 1.0),
        (0.1, 1.1103125),
        (0.2, 1.24283945),
        (0.3, 1.39974246),
        (0.4, 1.58364718),
        (0.5, 1.79740529),
        (0.6, 2.04415444),
        (0.7, 2.32735166),
        (0.8, 2.65082159),
        (0.9, 3.01878345),
        (1.0, 3.43590744),
        (1.1, 3.90734685),
        (1.2, 4.4387995)
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_ralston_specific()
    print("¡All tests passed!")