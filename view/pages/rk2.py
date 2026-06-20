import streamlit as st
import pandas as pd

from controller.runge_kutta_controller import RungeKuttaController
from controller.main_controller import MainController

main_controller = MainController({
    "runge_kutta": RungeKuttaController()
})


def show_rk2():

    st.header("Runge-Kutta Orden 2")

    f_expr = st.text_input(
        "Ingrese f(x,y)",
        value="x+y",
        key="rk2_f"
    )

    col1, col2 = st.columns(2)

    with col1:

        x0 = st.number_input(
            "x₀",
            value=0.0,
            key="rk2_x0"
        )

        y0 = st.number_input(
            "y₀",
            value=1.0,
            key="rk2_y0"
        )

    with col2:

        xf = st.number_input(
            "xf",
            value=1.0,
            key="rk2_xf"
        )

        n = st.number_input(
            "Número de pasos",
            min_value=1,
            value=10,
            key="rk2_n"
        )

    if st.button(
        "Calcular",
        key="rk2_btn"
    ):

        try:

            resultado = main_controller.execute_group(
                "runge_kutta",
                "rk2",
                f_expr,
                x0,
                y0,
                xf,
                int(n)
            )

            df = pd.DataFrame(
                resultado["points"],
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