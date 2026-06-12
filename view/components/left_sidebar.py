import streamlit as st

def left_sidebar():

    st.sidebar.title("Métodos")

    if "metodo" not in st.session_state:
        st.session_state.metodo = ("euler", "simple")
    selecion = None

    with st.sidebar.expander("Euler", expanded=True):
        if st.button("Euler Explícito"):
            st.session_state.metodo = ("euler", "simple")
        if st.button("Euler Mejorado"):
            st.session_state.metodo = ("euler", "mejorado")
        if st.button("Euler Implícito"):
            st.session_state.metodo = ("euler", "implicito")

    with st.sidebar.expander("Taylor", expanded=True):
        if st.button("Serie de Taylor"):
            st.session_state.metodo = ("taylor", "serie")

    
    return st.session_state.metodo

    