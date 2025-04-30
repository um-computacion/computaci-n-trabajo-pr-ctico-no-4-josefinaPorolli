import unittest

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.fibonacci import fibonacci_iterativo, fibonacci_recursivo

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_iterativo(self):
        self.assertEqual(fibonacci_iterativo(0), 0)
        self.assertEqual(fibonacci_iterativo(1), 1)
        self.assertEqual(fibonacci_iterativo(2), 1)
        self.assertEqual(fibonacci_iterativo(3), 2)
        self.assertEqual(fibonacci_iterativo(4), 3)
        self.assertEqual(fibonacci_iterativo(5), 5)
        self.assertEqual(fibonacci_iterativo(6), 8)
        self.assertEqual(fibonacci_iterativo(7), 13)
        self.assertEqual(fibonacci_iterativo(8), 21)
        self.assertEqual(fibonacci_iterativo(9), 34)
    
    def test_fibonacci_recursivo(self):
        self.assertEqual(fibonacci_recursivo(0), 0)
        self.assertEqual(fibonacci_recursivo(1), 1)
        self.assertEqual(fibonacci_recursivo(2), 1)
        self.assertEqual(fibonacci_recursivo(3), 2)
        self.assertEqual(fibonacci_recursivo(4), 3)
        self.assertEqual(fibonacci_recursivo(5), 5)
        self.assertEqual(fibonacci_recursivo(6), 8)
        self.assertEqual(fibonacci_recursivo(7), 13)
        self.assertEqual(fibonacci_recursivo(8), 21)
        self.assertEqual(fibonacci_recursivo(9), 34)

if __name__ == '__main__':
    unittest.main()