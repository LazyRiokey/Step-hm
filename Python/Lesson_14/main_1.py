""" Задание 1
К уже реализованному классу «Дробь» добавьте ста-
тический метод, который при вызове возвращает коли-
чество созданных объектов класса «Дробь».
"""


print()
print('Task 1'.center(40, '*'))
print()


class Fraction:

    counter = 0

    def __init__(self, nom_1, denom_1, nom_2, denom_2):
        self.nom_1 = nom_1
        self.denom_1 = denom_1
        self.nom_2 = nom_2
        self.denom_2 = denom_2
        self.result = None
        Fraction.counter += 1
    
    @staticmethod
    def fraction_count():
        return Fraction.counter
    
    def set_first_div(self):
        self.nom_1 = int(input('Введите числитель: '))
        self.denom_1 = int(input('Введите знаменатель: '))
    
    def set_second_div(self):
        self.nom_2 = int(input('Введите числитель: '))
        self.denom_2 = int(input('Введите знаменатель: '))
    
    def get_sum(self):
        if self.denom_1 == self.denom_2:
            self.result = (self.nom_1 + self.nom_2) / self.denom_1
        else:
            self.result = (((self.nom_1 * self.denom_2) + (self.nom_2 * self.denom_1)) / (self.denom_1 * self.denom_2))
        self.get_result()
    
    def get_sub(self):
        if self.denom_1 == self.denom_2:
            self.result = (self.nom_1 - self.nom_2) / self.denom_1
        else:
            self.result = (((self.nom_1 * self.denom_2) - (self.nom_2 * self.denom_1)) / (self.denom_1 * self.denom_2))
        self.get_result()
    
    def get_mult(self):
        self.result = (self.nom_1 * self.nom_2) / (self.denom_1 * self.denom_2)
        self.get_result()
    
    def get_div(self):
        self.result = (self.nom_1 * self.denom_2) / (self.denom_1 * self.nom_2)
        self.get_result()
    
    def get_result(self):
        print(self.result)


fract_obj_1 = Fraction(3, 4, 5, 6)
fract_obj_2 = Fraction(1, 5, 8, 9)

print(f'Количество созданных объектов класса \'Fraction\' >> {Fraction.fraction_count()}')


""" Задание 2
Создайте класс для конвертирования температуры из 
Цельсия в Фаренгейт и наоборот. У класса должно быть 
два статических метода: для перевода из Цельсия в Фа-
ренгейт и для перевода из Фаренгейта в Цельсий. Также 
класс должен считать количество подсчетов температуры и 
возвращать это значение с помощью статического метода.
"""


print()
print('Task 2'.center(40, '*'))
print()


class TemperatureConversion:

    counter = 0

    def __init__(self):
        TemperatureConversion.counter += 1

    @staticmethod
    def conversion_count():
        return TemperatureConversion.counter
    
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

temperature_1 = TemperatureConversion()
temperature_2 = TemperatureConversion()
print(f'{temperature_1.to_fahrenheit(15)}°F')
print(f'{temperature_1.to_celsius(15):.1f}°C')
print(f'{temperature_2.to_fahrenheit(40)}°F')
print(f'{temperature_2.to_celsius(40):.1f}°C')
print(f'Количество созданных объектов класса \'TemperatureConversion\' >> {TemperatureConversion.conversion_count()}')


""" Задание 3
Создайте класс для перевода из метрической системы 
в английскую и наоборот. Функциональность необходимо 
реализовать в виде статических методов. Обязательно 
реализуйте перевод мер длины.
"""


print()
print('Task 3'.center(40, '*'))
print()

# Дальнейшая информация взята с сайта:
# http://temperatures.ru/pages/perevod_angliiskih_mer

class Converter:

    """ Linear measures """

    @staticmethod
    def inches_to_centimeters(inches):
        return inches * 2.539
    
    @staticmethod
    def centimeters_to_inches(centimeters):
        return centimeters * 0.3937

    @staticmethod
    def feet_to_meters(feet):
        return feet * 0.3048
    
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.281
    
    @staticmethod
    def yards_to_meters(yards):
        return yards * 0.9144
    
    @staticmethod
    def meters_to_yards(meters):
        return meters * 1.094
    
    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.609
    
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.6214
    
    """ Measures of area """

    @staticmethod
    def sq_inches_to_sq_centimeters(sq_inches):
        return sq_inches * 6.452
    
    @staticmethod
    def sq_centimeters_to_sq_inches(sq_centimeters):
        return sq_centimeters * 0.1550
    
    @staticmethod
    def sq_meters_to_sq_feet(sq_meters):
        return sq_meters * 10.76
    
    @staticmethod
    def sq_feet_to_sq_meters(sq_feet):
        return sq_feet * 0.0929
    
    @staticmethod
    def sq_yards_to_sq_meters(sq_yards):
        return sq_yards * 0.8361
    
    @staticmethod
    def sq_meters_to_sq_yards(sq_meters):
        return sq_meters * 1.196
    
    @staticmethod
    def sq_miles_to_sq_kilometers(sq_miles):
        return sq_miles * 2.590
    
    @staticmethod
    def sq_kilometers_to_sq_miles(sq_kilometers):
        return sq_kilometers * 0.3861
    
    @staticmethod
    def sq_acres_to_sq_hectares(sq_acres):
        return sq_acres * 0.4047
    
    @staticmethod
    def sq_hectares_to_sq_acres(sq_hectares):
        return sq_hectares * 2.471
    
    """ Measures of volume """

    @staticmethod
    def cub_inches_to_cub_centimeters(cub_inches):
        return cub_inches * 16.39
    
    @staticmethod
    def cub_centimeters_to_cub_inches(cub_centimeters):
        return cub_centimeters * 0.06102
    
    @staticmethod
    def cub_feet_to_cub_meters(cub_feet):
        return cub_feet * 0.02832
    
    @staticmethod
    def cub_meters_to_cub_feet(cub_meters):
        return cub_meters * 35.31
    
    @staticmethod
    def cub_yards_to_cub_meters(cub_yards):
        return cub_yards * 0.7646
    
    @staticmethod
    def cub_meters_to_cub_yards(cub_meters):
        return cub_meters * 1.308
    
    @staticmethod
    def cub_inches_to_cub_liters(cub_inches):
        return cub_inches * 0.01639
    
    @staticmethod
    def cub_liters_to_cub_inches(cub_liters):
        return cub_liters * 61.03
    
    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * 4.546
    
    @staticmethod
    def liters_to_gallons(liters):
        return liters * 0.22
    
    """ Measures of weight """

    @staticmethod
    def grans_to_grams(grans):
        return grans * 0.0648
    
    @staticmethod
    def grams_to_grans(grams):
        return grams * 15.43
    
    @staticmethod
    def ounces_to_grams(ounces):
        return ounces * 28.35
    
    @staticmethod
    def grams_to_ounces(grams):
        return grams * 0.03527
    
    @staticmethod
    def pounds_to_grams(pounds):
        return pounds * 453.6
    
    @staticmethod
    def grams_to_pounds(grams):
        return grams * 0.002205
    
    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds * 0.4536
    
    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms * 2.205
    
conv_obj_1 = Converter()
print(conv_obj_1.centimeters_to_inches(5))
print(conv_obj_1.inches_to_centimeters(1.9685))