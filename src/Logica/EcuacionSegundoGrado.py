import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_x(self):
        # Calcula el discriminante
        discriminante = self.b ** 2 - 4 * self.a * self.c

        if discriminante < 0:
            return None  # CASO 3
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return x  # CASO 2
        else:
            # CASO 1
            x1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return x1, x2



