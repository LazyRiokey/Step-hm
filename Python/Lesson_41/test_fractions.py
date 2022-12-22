# Создайте класс по работе с дробями. В классе должна быть реализована следующая функциональность:
# - Сложение дробей;
# - Вычитание дробей;
# - Умножение дробей;
# - Деление дробей.
# Протестируйте все возможности созданного класса с помощью модульного тестирования (unittest).

from typing import Type
import unittest
from fractions import Fraction


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.fraction_1 = Fraction((5, 9))
        self.fraction_2 = Fraction((3, 8))

    def test_init(self):
        self.assertRaises(ValueError, self.fraction_1.__init__ or self.fraction_2.__init__, (0, 0))
        self.assertRaises(TypeError, self.fraction_1.__init__ or self.fraction_2.__init__, ("A", "B"))
        self.assertRaises(Exception, self.fraction_1.__init__ or self.fraction_2.__init__, ([0, 2, 3], [0, 5, 6, 7]))
        self.assertRaises(Exception, self.fraction_1.__init__ or self.fraction_2.__init__, ((0, "False", {1: "a",}), (0 ,5, True, "a")))


    # def test_add(self):
    #     self.assertEqual(self.fraction_1.add(self.fraction_2), "67/72")

    # def test_sub(self):
    #     self.assertEqual(self.fraction_1.add(self.fraction_2), "67/72")

    # def test_mul(self):
    #     self.assertEqual(self.fraction_1.add(self.fraction_2), "67/72")

    # def test_truediv(self):
    #     self.assertEqual(self.fraction_1.add(self.fraction_2), "67/72")
    
    # def test_type(self):
    #     self.assertRaises(TypeError, self.fraction_1.add, 23)
    #     self.assertRaises(TypeError, self.fraction_1.add, "hello")
    #     self.assertRaises(TypeError, self.fraction_1.add, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
