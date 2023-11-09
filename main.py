from src.Logica import EcuacionSegundoGrado

if __name__ == '__main__':

    ecuacion = EcuacionSegundoGrado.EcuacionCuadratica(1, -5, 1)
    soluciones = ecuacion.calcular_x()

    print("Soluciones:", soluciones)
