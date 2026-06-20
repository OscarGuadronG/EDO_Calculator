import streamlit as st
import pandas as pd

from controller.euler_controller import EulerController
from controller.main_controller import MainController

main_controller = MainController({
    "euler": EulerController()
})

def show_euler_explicito():

    st.header("Método de Euler Explícito")

    f_expr = st.text_input(
        "Ingrese f(x,y)",
        value="x+y"
    )

    col1, col2 = st.columns(2)

    with col1:
        x0 = st.number_input(
            "x₀",
            value=0.0
        )

        y0 = st.number_input(
            "y₀",
            value=1.0
        )

    with col2:
        xf = st.number_input(
            "xf",
            value=1.0
        )

        n = st.number_input(
            "Número de pasos",
            min_value=1,
            value=10
        )

    if st.button("Calcular"):

        try:

            resultado = main_controller.execute_group(
                "euler",
                "explicito",
                f_expr,
                x0,
                y0,
                xf,
                int(n)
            )

            resultados = resultado["points"]

            df = pd.DataFrame(
                resultados,
                columns=["x", "y"]
            )

            st.subheader("Tabla de resultados")
            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader("Gráfica")
            st.line_chart(
                df.set_index("x")["y"]
            )


        except Exception as e:
            st.error(f"Error: {e}")