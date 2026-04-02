from abc import ABC, abstractmethod

class BaseMethod(ABC):
    
    def __init__(self, f, x0, y0, h, xf):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.xf = xf

    def solve(self):
        x = self.x0
        y = self.y0
        results = [(x, y)]

        while x < self.xf:
            y = self.step(x, y)
            x = x + self.h

            results.append((x, y))

        return results

    @abstractmethod
    def step(self, x, y):
        pass