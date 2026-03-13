from abc import ABC, abstractmethod

class BaseMethod(ABC):
    @abstractmethod
    def solve(self, f, x0, y0, h, steps):
        """
        f: función diferencial f(x, y)
        x0: valor inicial de x
        y0: valor inicial de y
        h: tamaño del paso
        steps: número de iteraciones
        """
        pass

