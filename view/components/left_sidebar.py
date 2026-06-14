import streamlit as st

def left_sidebar():

    st.sidebar.title("Métodos")

    if "metodo" not in st.session_state:
        st.session_state.metodo = ("euler", "simple")
    selecion = None

    with st.sidebar.expander("Euler", expanded=True):
        if st.button("Hacia adelante"):
            st.session_state.metodo = ("euler", "simple")
        if st.button("Mejorado"):
            st.session_state.metodo = ("euler", "mejorado")
        if st.button("Hacia atrás"):
            st.session_state.metodo = ("euler", "implicito")

    with st.sidebar.expander("Taylor", expanded=True):
        if st.button("Serie de Taylor"):
            st.session_state.metodo = ("taylor", "serie")

    with st.sidebar.expander("Runge-Kutta", expanded=True):
        st.markdown("### Explicictos")
        if st.button("Punto medio"):
            st.session_state.metodo = ("runge-kutta", "punto_medio")
        if st.button("Ralston"):
            st.session_state.metodo = ("runge-kutta", "ralston")
        if st.button("RK2"):
            st.session_state.metodo = ("runge-kutta", "rk2")
            if st.button("RK3"):
                st.session_state.metodo = ("runge-kutta", "rk3")
            if st.button("RK4"):
                st.session_state.metodo = ("runge-kutta", "rk4")
        st.markdown("### Implícitos")
        if st.button("Gauss-Legendre"):
            st.session_state.metodo = ("runge-kutta", "gauss_legendre")
        if st.button("Trapecio"):
            st.session_state.metodo = ("runge-kutta", "trapecio")

    with st.sidebar.expander("Multipasos", expanded=True):
        st.markdown("### Adams-Bashforth")
        if st.button("Orden 2", key="bash_2"):
            st.session_state.metodo = ("multipasos", "bash_2")
        if st.button("Orden 3", key="bash_3"):
            st.session_state.metodo = ("multipasos", "bash_3")
        if st.button("Orden 4", key="bash_4"):
            st.session_state.metodo = ("multipasos", "bash_4")
        st.markdown("### Adams-Moulton")
        if st.button("Orden 2", key="moulton_2"):
            st.session_state.metodo = ("multipasos", "moulton_2")
        if st.button("Orden 3", key="moulton_3"):
            st.session_state.metodo = ("multipasos", "moulton_3")
        if st.button("Orden 4", key="moulton_4"):
                st.session_state.metodo = ("multipasos", "moulton_4")
        st.markdown("### Predictor-Corrector")
        if st.button("Predictor-Corrector"):
            st.session_state.metodo = ("multipasos", "predictor_corrector")

    return st.session_state.metodo

    