import pytest
import unittest

from SimpleCalc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        # naming convention is essential as 'test' the word that we need use when naming tests so python interpreter recognises it to run tests
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_substract(self):
        self.assertEqual(self.calc.substract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

