class Fraction:
    def __init__(self, data: tuple):
        try:
            self.numerator = data[0]
            self.denominator = data[1]
            self.drob = f"{self.numerator}/{self.denominator}"
        except:
            if data(0, 0):
                raise ValueError("Числитель или знаменатель не могут быть равны 0.")
            # elif self.numerator == 'A' or self.denominator == 'B':
            #     raise TypeError("Числитель или знаменатель должны быть цифрами.")

    def add(self, other):
        # Сложение дробей
        self.numerator = (self.numerator * other.denominator) + (
            other.numerator * self.denominator
        )
        self.denominator *= other.denominator
        self.drob = f"{self.numerator}/{self.denominator}"
        return self.drob

    def sub(self, other):
        # Вычитание дробей
        self.numerator = (self.numerator * other.denominator) - (
            other.numerator * self.denominator
        )
        self.denominator *= other.denominator
        self.drob = f"{self.numerator}/{self.denominator}"
        return self.drob

    def mul(self, other):
        # Умножение дробей
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self.drob = f"{self.numerator}/{self.denominator}"
        return self.drob

    def truediv(self, other):
        # Деление дробей
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        self.drob = f"{self.numerator}/{self.denominator}"
        return self.drob

    def __str__(self):
        return self.drob


f1 = Fraction((5, 9))

f2 = Fraction((9, 8))

print(f1.mul(f2))
