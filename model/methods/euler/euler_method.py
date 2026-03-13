from model.methods.base_method import BaseMethod

class EulerMethod(BaseMethod):
    def solve(self, f, x0, y0, h, steps):

        x = x0
        y = y0
        results = []

        for _ in range(steps):
            y = y + h * f(x, y)
            x = x + h

            results.append((x, y))

        return results