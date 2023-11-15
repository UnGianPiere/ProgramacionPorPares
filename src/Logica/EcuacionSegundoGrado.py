import math


class ExceptionDatos(Exception):
    pass


class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.lista = [a, b, c]
        self.validarNumeros()

    def calcular_x(self):
        # Calcula el discriminante
        discriminante = self.HallarDiscriminante()

        if discriminante < 0:
            # CASO 3: Raíces complejas
            parte_real = -self.b / (2 * self.a)
            parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * self.a)
            x1 = complex(parte_real, parte_imaginaria)
            x2 = complex(parte_real, -parte_imaginaria)
            # Redondear la parte imaginaria a 2 decimales
            x1 = complex(round(x1.real, 2), round(x1.imag, 2))
            x2 = complex(round(x2.real, 2), round(x2.imag, 2))
        elif discriminante == 0:
            # CASO 2: Raíces iguales
            x1 = round(-self.b / (2 * self.a), 2)
            x2 = x1
        else:
            # CASO 1: Raíces reales distintas
            x1 = round((-self.b + math.sqrt(discriminante)) / (2 * self.a), 2)
            x2 = round((-self.b - math.sqrt(discriminante)) / (2 * self.a), 2)

        return x1, x2

    def HallarDiscriminante(self):
        discriminante = self.b ** 2 - 4 * self.a * self.c
        return discriminante

    def validarNumeros(self):
        if self.lista is not None:
            for numero in self.lista:
                if not isinstance(numero, (int, float)):
                    raise ValueError("La lista debe contener solo números.")
        else:
            raise ExceptionDatos("La lista no puede ser None.")