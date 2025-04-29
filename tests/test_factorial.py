import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.factorial import factorial_interactivo, factorial_recursivo

class TestFactorial(unittest.TestCase):
    def test_factorial_interactivo(self):
        self.assertEqual(factorial_interactivo(0), 1)
        self.assertEqual(factorial_interactivo(1), 1)
        self.assertEqual(factorial_interactivo(5), 120)
        self.assertEqual(factorial_interactivo(10), 3628800)

    def test_factorial_recursivo(self):
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(10), 3628800)

if __name__ == '__main__':
    unittest.main()