
from model.methods.euler.euler_method import EulerMethod


def f(x, y):
    return x + y

def test_euler_method():
    x0 = 0
    y0 = 1
    h = 0.1
    xf = 0.5

    method = EulerMethod(f, x0, y0, h, xf)
    results = method.solve()

    expected_results = [
        (0.0, 1.0),
        (0.1, 1.1),
        (0.2, 1.22),
        (0.3, 1.362),
        (0.4, 1.5282),
        (0.5, 1.72102)
    ]

    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_euler_method()
    print("All tests passed!")