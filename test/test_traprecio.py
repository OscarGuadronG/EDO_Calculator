from model.methods.runge_kutta.Implicitos.traprecio_method import TrapecioMethod

def test_trapecio_specific():
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 1.2

    f_expr = "x + y"

    method = TrapecioMethod(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nNuevos valores calculados por el Método del Trapecio:")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 8)}),")

    # Valores teóricos calculados con el esquema implícito del Trapecio para x + y
    expected_results = [
        (0.0, 1.0),
        (0.1, 1.11052632),
        (0.2, 1.2431856),
        (0.3, 1.40040514),
        (0.4, 1.5846683),
        (0.5, 1.79883554),
        (0.6, 2.04603402),
        (0.7, 2.32974286),
        (0.8, 2.65380525),
        (0.9, 3.02247416),
        (1.0, 3.44044511),
        (1.1, 3.91273401),
        (1.2, 4.44512133)
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_trapecio_specific()
    print("¡All tests passed!")