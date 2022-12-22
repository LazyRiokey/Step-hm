import unittest
from math import pi
from fractions import Fraction
from calc_area import calc_area


class TestCalcArea(unittest.TestCase):

    def setUp(self):
        self.fraction = Fraction()

    def test_area(self):
        # Для проверки класса
        # self.assertEqual(self.fraction(3), pi * pow(3, 2))

        self.assertEqual(calc_area(3), pi * pow(3, 2))
        self.assertEqual(calc_area(1), pi)
        self.assertEqual(calc_area(0), 0)

    def test_value(self):
        self.assertRaises(ValueError, calc_area, -2)

    def test_type(self):
        self.assertRaises(TypeError, calc_area, [2+3j, 12, 45])
        self.assertRaises(TypeError, calc_area, True)
        self.assertRaises(TypeError, calc_area, "True")
        self.assertRaises(TypeError, calc_area, 3 + 2j)


if __name__ == "__main__":
    unittest.main()
