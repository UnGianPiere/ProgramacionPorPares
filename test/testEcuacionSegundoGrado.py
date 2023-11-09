import unittest
from src.Logica.EcuacionSegundoGrado import EcuacionCuadratica

class TestEcuacionCuadratica(unittest.TestCase):
    def setUp(self):
        self.ecuacion = EcuacionCuadratica(0, 0, 0)

    def tearDown(self):
        self.ecuacion = None

    def test_soluciones_reales(self):
        ecuacion1 = EcuacionCuadratica(1, -3, 2)
        self.assertEqual(ecuacion1.calcular_x(), (2, 1), "Error en test_soluciones_reales")

    def test_raiz_doble(self):
        ecuacion2 = EcuacionCuadratica(1, -4, 4)
        self.assertEqual(ecuacion2.calcular_x(), 2, "Error en test_raiz_doble")

    def test_sin_soluciones_reales(self):
        ecuacion3 = EcuacionCuadratica(1, 2, 5)
        self.assertIsNone(ecuacion3.calcular_x(), "Error en test_sin_soluciones_reales")

    def test_varios_casos(self):
        # Arrange
        casos = [
            {"coeficientes": (3, -5, 1), "soluciones": (1.43, 0.23)},


            {"coeficientes": (1, 0, -18), "soluciones": (4.24, -4.24)},




        ]

        for caso in casos:
            with self.subTest(coeficientes=caso["coeficientes"]):
                ecuacion = EcuacionCuadratica(*caso["coeficientes"])

                # Act
                resultado_actual = ecuacion.calcular_x()
                resultado_actual_rounded = tuple(round(val, 2) for val in resultado_actual)
                expected_rounded = caso["soluciones"]

                # Assert
                self.assertEqual(resultado_actual_rounded, expected_rounded)