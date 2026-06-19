import streamlit as st
from view.components.left_sidebar import left_sidebar
from view.pages.euler_explicito import show_euler_explicito
from view.pages.euler_implicito import show_euler_implicito
from view.pages.euler_mejorado import show_euler_mejorado
from view.pages.taylor import show_taylor
from view.pages.punto_medio import show_punto_medio
from view.pages.ralston import show_ralston
from view.pages.rk2 import show_rk2
from view.pages.rk3 import show_rk3
from view.pages.rk4 import show_rk4
from view.pages.gauss_legendre import show_gauss_legendre
from view.pages.trapecio import show_trapecio
from view.pages.adams_bashforth_2 import show_ab2
from view.pages.adams_bashforth_3 import show_ab3
from view.pages.adams_bashforth_4 import show_ab4
from view.pages.adams_moulton_2 import show_am2
from view.pages.adams_moulton_3 import show_am3
from view.pages.adams_moulton_4 import show_am4
from view.pages.predictor_corrector import show_predictor_corrector


st.set_page_config(
    page_title="Calculadora EDO",
    layout="wide"
)

st.title("Calculadora EDO")

grupo, metodo = left_sidebar()

if grupo == "euler":

    if metodo == "explicito":
        show_euler_explicito()

    elif metodo == "mejorado":
        show_euler_mejorado()

    elif metodo == "implicito":
        show_euler_implicito()

elif grupo == "taylor":

    if metodo == "serie":
        show_taylor()


elif grupo == "runge_kutta":

    if metodo == "punto_medio":
        show_punto_medio()

    elif metodo == "ralston":
        show_ralston()

    elif metodo == "rk2":
        show_rk2()

    elif metodo == "rk3":
        show_rk3()

    elif metodo == "rk4":
        show_rk4()

    elif metodo == "trapecio":
        show_trapecio()

    elif metodo == "gauss_legendre":
        show_gauss_legendre()

elif grupo == "multipasos":

    if metodo == "ab2":
        show_ab2()

    elif metodo == "ab3":
        show_ab3()

    elif metodo == "ab4":
        show_ab4()

    elif metodo == "am2":
        show_am2()

    elif metodo == "am3":
        show_am3()

    elif metodo == "am4":
        show_am4()

    elif metodo == "predictor_corrector":
        show_predictor_corrector()