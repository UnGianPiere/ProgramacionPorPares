import unittest
from src.Logica.EcuacionSegundoGrado import EcuacionCuadratica,ExceptionDatos

class TestEcuacionCuadratica(unittest.TestCase):
    def setUp(self):
        self.ecuacion = EcuacionCuadratica(0, 0, 0)

    def tearDown(self):
        self.ecuacion = None

    def test_varios_casosReales(self):
        # Arrange
        casos = [
            {"coeficientes": (3, -5, 1), "soluciones": (1.43, 0.23)},
            {"coeficientes": (1, 2, 1), "soluciones": (-1.00, -1.00)},
            {"coeficientes": (-1, 2, -1), "soluciones": (1.00, 1.00)},
            {"coeficientes": (1, 0, -18), "soluciones": (4.24, -4.24)},
            {"coeficientes": (1, 4, 0), "soluciones": (0.00, -4.00)},
            {"coeficientes": (1, 4, 4), "soluciones": (-2.00, -2.00)},
            {"coeficientes": (1, 3, 2), "soluciones": (-1.00, -2.00)},
        ]

        for caso in casos:
            with self.subTest(coeficientes=caso["coeficientes"]):
                ecuacion = EcuacionCuadratica(*caso["coeficientes"])

                # Act
                resultado_actual = ecuacion.calcular_x()
                expected_rounded = caso["soluciones"]

                # Assert
                self.assertEqual(resultado_actual, expected_rounded)

    def test_varios_casosComplejos(self):
        # Arrange
        casos = [
            {"coeficientes": [1, 1, 1], "soluciones": ((-0.5+0.87j), (-0.5-0.87j))},
            {"coeficientes": [1, 2, 3], "soluciones": ((-1.0+1.41j), (-1.0-1.41j))}
        ]

        for caso in casos:
            with self.subTest(coeficientes=caso["coeficientes"]):
                ecuacion = EcuacionCuadratica(*caso["coeficientes"])

                # Act
                resultado_actual = ecuacion.calcular_x()
                expected_rounded = caso["soluciones"]

                # Assert
                self.assertEqual(resultado_actual, expected_rounded)



    def test_varios_casosInvalidos(self):
        # Arrange
        casos = [
            {"coeficientes": ['a', 'b', 'c']},
            {"coeficientes": ['a', 1, 1]},
            {"coeficientes": [1, 'aa', 3]},
            {"coeficientes": [1, '3.1', 3]},
        ]

        for caso in casos:
            with self.subTest(coeficientes=caso["coeficientes"]):
                with self.assertRaises(ValueError):
                    ecuacion = EcuacionCuadratica(*caso["coeficientes"])
                    ecuacion.calcular_x()
