from model.methods.base_method import BaseMethod

class EulerMethod(BaseMethod):
    
    def step(self, x, y):
        return y + self.h * self.f(x, y)