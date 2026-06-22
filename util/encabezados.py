

class Encabezado:
    def encabezado(self, grupo, metodo):
        if (grupo == "euler"):
            if (metodo == "explicito"):
                return "Euler Hacia Adelante"
            if (metodo == "mejorado"):
                return "Euler Mejorado"
            if (metodo == "implicito"):
                return "Euler Hacia Atrás"
        if (grupo == "taylor"):
            if (metodo == "serie"):
                return "Serie de Taylor"
        if (grupo == "runge_kutta"):
            if (metodo == "punto_medio"):
                return "Runge-Kutta: Punto Medio"
            if (metodo == "ralston"):
                return "Runge-Kutta: Ralston"
            if (metodo == "rk2"):
                return "Runge-Kutta: Orden 2"
            if (metodo == "rk3"):
                return "Runge-Kutta: Orden 3"
            if (metodo == "rk4"):
                return "Runge-Kutta: Orden 4"
            if (metodo == "trapecio"):
                return "Runge-Kutta: Trapecio"
            if (metodo == "gauss_legendre"):
                return "Runge-Kutta: Gauss-Legendre"
        if (grupo == "multipasos"):
            if (metodo == "ab2"):
                return "Adams-Bashforth de 2 pasos"
            if (metodo == "ab3"):
                return "Adams-Bashforth de 3 pasos"
            if (metodo == "ab4"):
                return "Adams-Bashforth de 4 pasos"
            if (metodo == "am2"):
                return "Adams-Moulton de 2 pasos"
            if (metodo == "am3"):
                return "Adams-Moulton de 3 pasos"
            if (metodo == "am4"):
                return "Adams-Moulton de 4 pasos"
            if (metodo == "predictor_corrector"):
                return "Predictor-Corrector"
        return f"{grupo}: {metodo}"