from model.methods.multipasos.adams_bashfoth.adams_bashforth_3_method import AdamsBashforth3Method

def test_ejercicio_imagen():
    # Parámetros extraídos del problema
    x0 = 0.0
    y0 = -1.0
    xf = 2.0
    h = 0.5  # Para lograr exactamente 5 puntos en el intervalo [0, 2]

    # Ecuación diferencial con la derivada despejada
    f_expr = "(3*x**2 + 4*x - 2) / (2*(y - 1))"

    method = AdamsBashforth3Method(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nResultados para el ejercicio de Adams-Bashforth 3 (5 puntos):")
    print("--------------------------------------------------")
    print(f"{'Punto':<8}{'x (t)':<12}{'y aproximado':<15}")
    print("--------------------------------------------------")
    for idx, r in enumerate(results):
        print(f"{idx+1:<8}{round(r[0], 2):<12}{round(r[1], 8):<15}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    test_ejercicio_imagen()