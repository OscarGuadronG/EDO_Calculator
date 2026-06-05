
from model.methods.euler.euler_Mejorado_method import EulerMethod




def test_euler_mejorado_method():
    x0 = 1
    y0 = 1
    h = 0.1
    xf = 1.5
    f_expr = "2*x*y"
    method = EulerMethod(f_expr, x0, y0, h, xf)
    results = method.solve()

    results = method.solve()

    print("\nNuevos valores calculados por SymPy:")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 9)}),")

    expected_results = [
        (1.0, 1.0),
        (1.1, 1.232),
        (1.2, 1.5478848),
        (1.3, 1.983150006),
        (1.4, 2.590787168),
        (1.5, 3.450928507),
        (1.6, 4.686360913)
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_euler_mejorado_method()
    print("All tests passed!")