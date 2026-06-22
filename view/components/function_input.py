import streamlit as st
import sympy as sp

from util.sympy_parse import parse_user_function, preprocess_expression

def _insert_token(token: str):
    st.session_state.math_function += token

def render_math_function_input(
    label: str = "Ingrese f(x,y)",
    default_value: str = "x+y"
):
    if "math_function" not in st.session_state:
        st.session_state.math_function = default_value

    user_input = st.text_input(
        label,
        key="math_function"
    )

    func_col, opr_col = st.columns(2)
    FUNCTION_BUTTONS = [
        [("sin", "sin("), ("cos", "cos("), ("tan", "tan(")],
        [("ln", "ln("), ("log10", "log10("), ("√", "sqrt(")],
        [("π", "π"), ("e", "e"), None]
    ]
    OPERATOR_BUTTONS = [
        [("+", "+"), ("-", "-"), ("*", "*")],
        [("/", "/"), ("^", "^"), ("x", "x")],
        [("(", "("), (")", ")"), ("y", "y")]
        ]
    with func_col:
        for row in FUNCTION_BUTTONS:
            cols = st.columns(3)

            for col, button_data in zip(cols, row):
                with col:
                    if button_data is not None:
                        label, token = button_data
                        st.button(
                            label, on_click=_insert_token, args=(token,)
                        )
    with opr_col:
        for row in OPERATOR_BUTTONS:
            cols = st.columns(3)

            for col, button_data in zip(cols, row):
                with col:
                    if button_data is not None:
                        label, token = button_data
                        st.button(
                            label, on_click=_insert_token, args=(token,)
                        )

    st.button("Limpiar", on_click=clear_function)

    if not user_input.strip():
        return None
    
    try:
        expr = preprocess_expression(user_input)
        expr = parse_user_function(expr)
        return expr
    except Exception :
        return None
    
def clear_function():
    st.session_state.math_function = ""
