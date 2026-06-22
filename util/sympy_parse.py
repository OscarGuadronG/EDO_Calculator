import re

from sympy import symbols, E, pi
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)

x, y = symbols('x y')

TRANSFORMATIONS = (
    standard_transformations
    + (
        implicit_multiplication_application,
        convert_xor,
    )
)

LOCAL_DICT = {
    "x": x,
    "y": y,
    "e": E,
    "E": E,
    "pi": pi
}

def parse_user_function(expression: str):
    return parse_expr(
        expression,
        local_dict=LOCAL_DICT,
        transformations=TRANSFORMATIONS
    )

def preprocess_expression(expr: str) -> str:

    # ln(x) -> log(x)
    expr = re.sub(
        r"\bln\s*\(",
        "log(",
        expr
    )

    # log10(x) -> log(x,10)
    expr = re.sub(
        r"log10\s*\((.*?)\)",
        r"log(\1,10)",
        expr
    )

    expr = expr.replace("π", "pi")

    expr = expr.replace("√", "sqrt")

    return expr