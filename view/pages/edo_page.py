from ast import expr

import streamlit as st
import pandas as pd

from controller.main_controller import MainController
from view.components.function_input import render_math_function_input

def show_edo_page(main_controller, grupo, metodo):

    f_expr = render_math_function_input()

    col1, col2 = st.columns(2)
    with col1:
        x0 = st.number_input(
            "x₀", value=0.0
        )
        y0 = st.number_input(
            "y₀", value=1.0
        )
    with col2:
        xf = st.number_input(
            "xf", value=1.0
        )
        n = st.number_input(
            "Número de pasos",
            min_value=1, value=5
        )
    
    h = (xf - x0) / n if n != 0 else 0
    st.subheader(f"h = {h:.8f}")

    if st.button("Calcular"):
        if f_expr is None:
            st.error("Por favor, ingrese una función válida.")
            return
        try:
            resultado = main_controller.execute_group(
                grupo, metodo, f_expr, x0, y0, xf, int(n)
            )

            resultados = resultado["points"]

            df = pd.DataFrame(
                resultados, columns=["x", "y"]
            )

            st.subheader("Tabla de resultados")
            st.dataframe(
                df, use_container_width=True
            )

            yf_final = resultado["y"][-1]
            st.subheader("Resultado final")
            st.metric(
                label=f"y({xf})", value=f"{yf_final:.8f}"
            )
            
            st.subheader("Gráfica")
            st.line_chart(
                df.set_index("x")["y"]
            )

        except Exception as e:
            st.error(f"Error: {e}")
        