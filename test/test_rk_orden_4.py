from model.methods.runge_kutta.Explicitos.rk_orden_4_method import RK4Method

def test_rk4_specific():
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 1.2

    f_expr = "x + y"

    method = RK4Method(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nNuevos valores calculados por RK4:")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 8)}),")

    # Valores teóricos de RK4 con alta precisión para x + y
    expected_results = [
        (0.0, 1.0),
        (0.1, 1.11034167),
        (0.2, 1.24280552),
        (0.3, 1.39971761),
        (0.4, 1.5836494),
        (0.5, 1.79744254),
        (0.6, 2.0442376),
        (0.7, 2.32750541),
        (0.8, 2.65108185),
        (0.9, 3.01920622),
        (1.0, 3.43656365),
        (1.1, 3.90817033),
        (1.2, 4.43979601)
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_rk4_specific()
    print("¡All tests passed!")