from model.methods.multipasos.Adams_Moulton.adams_moulton_4_method import AdamsMoulton4Method

def test_adams_moulton_4_imagen():
    x0 = 0.0
    y0 = -1.0
    xf = 2.0
    h = 0.5  # Genera 5 puntos en [0, 2]

    f_expr = "(3*x**2 + 4*x - 2) / (2*(y - 1))"

    method = AdamsMoulton4Method(f_expr, x0, y0, h, xf)
    results = method.solve()

    print("\nResultados para el ejercicio usando Adams-Moulton 4 (Predictor-Corrector):")
    print("--------------------------------------------------")
    print(f"{'Punto':<8}{'x (t)':<12}{'y aproximado':<15}")
    print("--------------------------------------------------")
    for idx, r in enumerate(results):
        print(f"{idx+1:<8}{round(r[0], 2):<12}{round(r[1], 8):<15}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    test_adams_moulton_4_imagen()