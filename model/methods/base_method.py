from abc import ABC, abstractmethod
from pyparsing import results

class BaseMethod(ABC):
    def __init__(self, f, x0, y0, h, n, xf):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        if xf == x0:
            raise ValueError("xf debe ser distinto de x0") 
        self.h = h
        self.n = n
        if n <= 0:
            raise ValueError("n debe ser un entero positivo")
        self.xf = xf

    def solve(self):
        x = self.x0
        y = self.y0

        results = [(x, y)]

        while len(results) <= self.n:
            y = self.step(x, y)
            x = x + self.h
            results.append((x, y))

        return results

    @abstractmethod
    def step(self, x, y):
        pass