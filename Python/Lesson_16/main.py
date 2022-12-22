""" Task 1 """

# import datetime as dt


# class Simple:

#     def __init__(self, func):
#         self.func = func
    
#     def __call__(self):
#         cur_time = dt.datetime.now()
#         return f'{self.func()}\n {dt.datetime.now() - cur_time}' 

# @Simple
# def prime_numbers(numbers=1000):
#     prime_list = []
    
#     for i in range(2, numbers+1):
#         if all(i % n != 0 for n in range(2, i)):
#             prime_list.append(i)
    
#     return prime_list

# print(prime_numbers())


""" Task 2 """

""" Объявите класс Calendar для хранения даты: день, месяц, год.
Опредлите свойства для записи и считывания этой информации из этого класса.
"""


# class CalendarDescriptor:

#     def __set_name__(self, owner, name):
#         self.name = name
    
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
    
#     def __set__(self, instance, value):
#         if isinstance(value, int) and value > 0:
#             if self.name == 'day' or self.name == 'month':
#                 if value < 9:
#                     value = str(value).rjust(2, '0')
#         else:
#             raise ValueError('Что-то пошло не так...')
#         instance.__dict__[self.name] = str(value)    
            
#     # def __delete__(self, object):
#     #     del object.__dict__[self.__name]


# class Calendar:
#     day = CalendarDescriptor()
#     month = CalendarDescriptor()
#     year = CalendarDescriptor()

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
    
#     def total(self):
#         return f'{self.day}.{self.month}.{self.year}'

# date_1 = Calendar(1, 2, 1990)
# date_2 = Calendar(2, 3, 2019)

# print(date_1.day, date_1.month, date_1.year)
# print(date_2.day, date_2.month, date_2.year)


""" Task 3 """

""" Объявите класс Rectangle, хранящий координаты верхней левой и правой нижней точек. 
Создайте дескрипторы для записи и считывания этих значений в классе
(атрибуты с данными координатами должны быть приватными)."""


# class RectangleDescriptor:

#     def __set_name__(self, owner, name):
#         self.__name = name
    
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
    
#     def __set__(self, instance, value):
#         if isinstance(value, int):
#             instance.__dict__[self.__name] = value
#         else:
#             raise ValueError('Что-то пошло не так...')
    
    # def __delete__(self, object):
    #     del object.__dict__[self.__name]


# class Rectangle:
#     x1 = RectangleDescriptor()
#     y1 = RectangleDescriptor()
#     x2 = RectangleDescriptor()
#     y2 = RectangleDescriptor()

#     def __init__(self, x1, y1, x2, y2):
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2


# dots_obj_1 = Rectangle(1, 1, 3, 3)
# dots_obj_2 = Rectangle(5, 6, 1, 2)

# print(dots_obj_1.__dict__)
# print(dots_obj_2.__dict__)

# dots_obj_1.x1 = 8
# dots_obj_2.y2 = 4

# print(dots_obj_1.x1)
# print(dots_obj_2.y2)

