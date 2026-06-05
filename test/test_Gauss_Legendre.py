from model.methods.runge_kutta.Implicitos.Gauss_Legendre_method import GaussLegendreMethod

def test_gauss_legendre_specific():
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 1.2

    f_expr = "x + y"

    method = GaussLegendreMethod(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nNuevos valores calculados por Gauss-Legendre:")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 8)}),")

    # Valores teóricos base de alta precisión
    expected_results = [
        (0.0, 1.0),
        (0.1, 1.11034184),
        (0.2, 1.2428059),
        (0.3, 1.39971816),
        (0.4, 1.58365017),
        (0.5, 1.79744358),
        (0.6, 2.04423901),
        (0.7, 2.32750731),
        (0.8, 2.65108439),
        (0.9, 3.01920953),
        (1.0, 3.43656793),
        (1.1, 3.90817578),
        (1.2, 4.4398028)
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_gauss_legendre_specific()
    print("¡All tests passed!")