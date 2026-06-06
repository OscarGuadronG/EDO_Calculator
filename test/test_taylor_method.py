# Guardar en test/test_taylor_method.py
from model.methods.taylor.taylor_method import TaylorSecondOrderAutoMethod

def test_taylor_ejercicio_imagenes():
    # Parámetros extraídos de las imágenes
    x0 = 0.0
    y0 = 2.0
    h = 0.2
    xf = 1.0

    # Expresión matemática compatible con SymPy
    f_expr = "(x**2 + 1) / y"

    # Instanciamos el método automático
    method = TaylorSecondOrderAutoMethod(f_expr, x0, y0, h, xf)
    results = method.solve()

    # Datos exactos impresos en la consola de tu imagen
    expected_results = [
        (0.0, 2.000000),
        (0.2, 2.097500),
        (0.4, 2.198136),
        (0.6, 2.308425),
        (0.8, 2.433643),
        (1.0, 2.577838)
    ]

    # Imprimir para depuración visual en la terminal
    print(f"\n{'i':<3} | {'x':<10} | {'y calculado':<15} | {'y esperado (MATLAB)':<15}")
    print("-" * 55)
    for i, (res, exp) in enumerate(zip(results, expected_results)):
        print(f"{i:<3} | {res[0]:<10.6f} | {res[1]:<15.6f} | {exp[1]:<15.6f}")

    # Validaciones con tolerancia por precisión de coma flotante
    for result, expected in zip(results, expected_results):
        assert abs(result[0] - expected[0]) < 1e-6
        assert abs(result[1] - expected[1]) < 1e-6

if __name__ == "__main__":
    test_taylor_ejercicio_imagenes()
    print("\n¡El test de Taylor con los datos de las imágenes pasó con éxito!")