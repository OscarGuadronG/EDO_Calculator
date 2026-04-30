class euler_controller:

    def __init__(self, model):
        self.model = model

    def execute(self, method, f, x0, y0, h, n):
        """
        metodo: string -> "explicito", "mejorado", "implicito"
        """
        if method == "explicito":
            return self.model.euler_method(f, x0, y0, h, n)
        else:
            raise ValueError("Metodo no soportado")