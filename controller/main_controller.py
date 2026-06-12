class MainController:
    def __init__(self, controller):
        self.controllers = controller

    def execute_group(self, group, method, f, x0, y0, xf, n, **keywargs):
        h=(xf - x0) / n
        controller = self.controllers.get(group)
        
        if not controller:
            raise ValueError(f"Grupo '{group}' no soportado")
        return controller.execute(method, f, x0, y0, h, xf, **keywargs)
