import unittest
from api import ConjuntoNumeros

class TestConjuntoNumeros(unittest.TestCase):
    def setUp(self):
        self.conjunto = ConjuntoNumeros()

    def test_extract_valid_number(self):
        self.conjunto.extract(50)
        self.assertNotIn(50, self.conjunto.numeros)
        self.assertEqual(self.conjunto.extraido, 50)

    def test_extract_invalid_number_below_range(self):
        with self.assertRaises(ValueError):
            self.conjunto.extract(0)

    def test_extract_invalid_number_above_range(self):
        with self.assertRaises(ValueError):
            self.conjunto.extract(101)

    def test_extract_number_already_extracted(self):
        self.conjunto.extract(50)
        with self.assertRaises(ValueError):
            self.conjunto.extract(50)

    def test_calcular_numero_faltante(self):
        self.conjunto.extract(75)
        numero_faltante = self.conjunto.calcular_numero_faltante()
        self.assertEqual(numero_faltante, 75)

    def test_calcular_numero_faltante_sin_extraccion(self):
        with self.assertRaises(ValueError):
            self.conjunto.calcular_numero_faltante()

    def test_input_no_entero(self):
        with self.assertRaises(ValueError):
            self.conjunto.extract("string")

if __name__ == '__main__':
    unittest.main()