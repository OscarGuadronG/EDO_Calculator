# Importación corregida con la ruta exacta de tus carpetas
from model.methods.multipasos.adams_bashfoth.adams_bashforth_2_method import AdamsBashforth2Method

def test_adams_bashforth_specific():
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    xf = 1.2

    f_expr = "x + y"

    method = AdamsBashforth2Method(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nNuevos valores calculados por Adams-Bashforth 2:")
    print("--------------------------------------------------")
    for r in results:
        print(f"({round(r[0], 2)}, {round(r[1], 8)}),")
    print("--------------------------------------------------")

if __name__ == "__main__":
    test_adams_bashforth_specific()
    print("¡Ejecución completada con éxito!")