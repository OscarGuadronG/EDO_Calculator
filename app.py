import streamlit as st
from view.components.left_sidebar import left_sidebar

st.title("Calculadora EDO")


grupo,method = left_sidebar()

st.write(f"Grupo: {grupo}")
st.write(f"Método: {method}")

if grupo == "euler" and method == "simple":
    st.write("Has seleccionado el método de Euler Explícito.")
elif grupo == "euler" and method == "mejorado":
    st.write("Has seleccionado el método de Euler Mejorado.")

