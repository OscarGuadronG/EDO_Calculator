import streamlit as st


def left_sidebar():

    st.sidebar.title("Métodos Numéricos")

    if "metodo" not in st.session_state:
        st.session_state.metodo = ("euler", "explicito")

    # EULER
    with st.sidebar.expander("Euler", expanded=True):

        if st.button("Euler Explícito", use_container_width=True):
            st.session_state.metodo = ("euler", "explicito")

        if st.button("Euler Mejorado", use_container_width=True):
            st.session_state.metodo = ("euler", "mejorado")
        if st.button("Hacia atrás"):
            st.session_state.metodo = ("euler", "implicito")

        if st.button("Euler Implícito", use_container_width=True):
            st.session_state.metodo = ("euler", "implicito")

    # TAYLOR
    with st.sidebar.expander("Taylor", expanded=False):

        if st.button("Serie de Taylor", use_container_width=True):
            st.session_state.metodo = ("taylor", "serie")

    # RUNGE-KUTTA
    with st.sidebar.expander("Runge-Kutta", expanded=False):

        with st.expander("Explícitos", expanded=False):

            if st.button("Punto Medio", use_container_width=True):
                st.session_state.metodo = (
                    "runge_kutta",
                    "punto_medio"
                )

            if st.button("Ralston", use_container_width=True):
                st.session_state.metodo = (
                    "runge_kutta",
                    "ralston"
                )

            if st.button("RK Orden 2", use_container_width=True):
                st.session_state.metodo = (
                    "runge_kutta",
                    "rk2"
                )

            if st.button("RK Orden 3", use_container_width=True):
                st.session_state.metodo = (
                    "runge_kutta",
                    "rk3"
                )

            if st.button("RK Orden 4", use_container_width=True):
                st.session_state.metodo = (
                    "runge_kutta",
                    "rk4"
                )

        with st.expander("Implícitos", expanded=False):

            if st.button("Trapecio", use_container_width=True):
                st.session_state.metodo = (
                    "runge_kutta",
                    "trapecio"
                )

            if st.button("Gauss-Legendre", use_container_width=True):
                st.session_state.metodo = (
                    "runge_kutta",
                    "gauss_legendre"
                )

    # MULTIPASOS
    with st.sidebar.expander("Multipasos",expanded=False):

        with st.expander("Adams-Bashforth",expanded=False):

            if st.button("Adams-Bashforth 2",use_container_width=True):
                st.session_state.metodo = (
                    "multipasos",
                    "ab2"
                )

            if st.button("Adams-Bashforth 3",use_container_width=True):
                st.session_state.metodo = (
                    "multipasos",
                    "ab3"
                )

            if st.button("Adams-Bashforth 4",use_container_width=True):
                st.session_state.metodo = (
                    "multipasos",
                    "ab4"
                )

        with st.expander("Adams-Moulton",expanded=False):

            if st.button("Adams-Moulton 2",use_container_width=True):
                st.session_state.metodo = (
                    "multipasos",
                    "am2"
                )

            if st.button("Adams-Moulton 3",use_container_width=True):
                st.session_state.metodo = (
                    "multipasos",
                    "am3"
                )

            if st.button("Adams-Moulton 4",use_container_width=True):
                st.session_state.metodo = (
                    "multipasos",
                    "am4"
                )

        with st.expander("Predictor-Corrector",expanded=False):

            if st.button("Predictor-Corrector",use_container_width=True):
                st.session_state.metodo = (
                    "multipasos",
                    "predictor_corrector"
                )
    return st.session_state.metodo