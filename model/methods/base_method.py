from abc import ABC, abstractmethod

class BaseMethod(ABC):
    
    def __init__(self, f, x0, y0, h, n):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        if h == 0:
            raise ValueError("El paso h debe distinto de 0")    
        self.h = h
        if n <= 0:
            raise ValueError("n no puede ser menor o igual a 0")    
        self.n = n
    
    @property
    def xf(self):
        return self.x0 + self.n * self.h

    def solve(self):
        x = self.x0
        y = self.y0
        results = [(x, y)]

        for i in range(self.n):
            y = self.step(x, y)
            x = x + self.h

            results.append((x, y))

        return results

    @abstractmethod
    def step(self, x, y):
        pass