import streamlit as st

from controller.euler_controller import EulerController
from controller.main_controller import MainController
from controller.multipasos_controller import MultipasosController
from controller.runge_kutta_controller import RungeKuttaController
from controller.taylor_controller import TaylorController
from view.components.left_sidebar import left_sidebar
from view.pages.edo_page import show_edo_page

main_controller = MainController({
    "euler": EulerController(),
    "taylor": TaylorController(),
    "runge_kutta": RungeKuttaController(),
    "multipasos": MultipasosController()
})

st.set_page_config(
    page_title="Calculadora EDO",
    layout="wide"
)

st.title("Calculadora EDO")

grupo, metodo = left_sidebar()

if grupo != "taylor" and metodo != "serie":
    show_edo_page(main_controller, grupo, metodo)