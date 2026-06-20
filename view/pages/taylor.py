import streamlit as st
import pandas as pd

from controller.taylor_controller import TaylorController
from controller.main_controller import MainController

main_controller = MainController({
    "taylor": TaylorController()
})


def show_taylor():

    st.header("Método de Taylor de Segundo Orden")

    f_expr = st.text_input(
        "Ingrese f(x,y)",
        value="x+y",
        key="taylor_f"
    )

    col1, col2 = st.columns(2)

    with col1:

        x0 = st.number_input(
            "x₀",
            value=0.0,
            key="taylor_x0"
        )

        y0 = st.number_input(
            "y₀",
            value=1.0,
            key="taylor_y0"
        )

    with col2:

        xf = st.number_input(
            "xf",
            value=1.0,
            key="taylor_xf"
        )

        n = st.number_input(
            "Número de pasos",
            min_value=1,
            value=10,
            key="taylor_n"
        )

    if st.button(
        "Calcular",
        key="taylor_btn"
    ):

        try:

            resultado = main_controller.execute_group(
                "taylor",
                "serie",
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