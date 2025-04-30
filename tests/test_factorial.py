import unittest

# Para detectar el archivo que implementa las las funciones
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.factorial import factorial_iterativo, factorial_recursivo

class TestFactorial(unittest.TestCase): # crear la clase unittest
    def test_factorial_iterativo(self): # crear la función test para factorial_iterativo
        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(1), 1)
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(10), 3628800)

    def test_factorial_recursivo(self): # crear la función test para factorial_recursivo
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(10), 3628800)

# ejecutar el test
if __name__ == '__main__':
    unittest.main()