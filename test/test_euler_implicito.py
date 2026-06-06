from model.methods.euler.euler_implicito import Euler_Implicit_Method


def test_euler_implicit_specific():
  
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 1.2  

   
    f_expr = "x + y"

    method = Euler_Implicit_Method(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\n==========================================")
    print("      VALORES CALCULADOS POR EL CÓDIGO    ")
    print("==========================================")
    for r in results:
        print(f"x = {r[0]:.1f}  ->  y = {r[1]:.9f}")
    print("==========================================\n")

    expected_results = [
        (0.0, 1.0),
        (0.1, 1.122222222),
        (0.2, 1.269135802),
        (0.3, 1.443484224),
        (0.4, 1.648315805),
        (0.5, 1.887017561),
        (0.6, 2.163352845),
        (0.7, 2.481503161),
        (0.8, 2.845781291),
        (0.9, 3.261201444),
        (1.0, 3.733557152),
        (1.1, 4.269507945),
        (1.2, 4.876119939),
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6


if __name__ == "__main__":
    test_euler_implicit_specific()
    print("¡All tests passed!")