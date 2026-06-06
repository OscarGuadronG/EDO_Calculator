from model.methods.runge_kutta.Explicitos.punto_medio import RK2MidpointMethod

def test_rk2_midpoint_specific():
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 1.2

    f_expr = "x + y"

    method = RK2MidpointMethod(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nNuevos valores calculados por RK2 Punto Medio:")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 8)}),")

    expected_results = [
        (0.0, 1.0),
        (0.1, 1.11),
        (0.2, 1.24205),
        (0.3, 1.39846525),
        (0.4, 1.5818041),
        (0.5, 1.79489353),
        (0.6, 2.04085735),
        (0.7, 2.32314737),
        (0.8, 2.64557785),
        (0.9, 3.01236352),
        (1.0, 3.42816169),
        (1.1, 3.89811867),
        (1.2, 4.42792113)
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_rk2_midpoint_specific()
    print("¡All tests passed!")