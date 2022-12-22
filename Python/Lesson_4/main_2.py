""" Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
"""

import random

print()
print('Task 1'.center(40, '*'))
print()

genList_1 = [random.randint(-100, 100) for i in range(random.randrange(100))]
genList_2 = [random.randint(-100, 100) for i in range(random.randrange(100))]

"""Сформировать третий список, содержащий элементы
обоих списков """

print()
print('Task 1.1'.center(40, '*'))
print()

genList_3 = genList_1 + genList_2

print(f"List containing elements both lists:\n{genList_3}")

""" Сформировать третий список, содержащий элементы
обоих списков без повторений """

print()
print('Task 1.2'.center(40, '*'))
print()

genList_4 = list(set(genList_3))

print(f"List containing elements both lists without repetition:\n{genList_4}")

""" Сформировать третий список, содержащий элементы
общие для двух списков """

print()
print('Task 1.3'.center(40, '*'))
print()

genList_5 = [i for i in genList_3 if i in genList_1 and i in genList_2]

print(f"List containing elements common to two lists:\n{genList_5}")

""" Сформировать третий список, содержащий только
уникальные элементы каждого из списков """

# Решил разбить длинную строку на несколько
# отдельных переменных для наглядности.

print()
print('Task 1.4'.center(40, '*'))
print()

tmpList_1 = [i for i in genList_1 if i not in genList_2]
tmpList_2 = [i for i in genList_2 if i not in genList_1]
genList_6 = tmpList_1 + tmpList_2

print(f"List containing only unique elements of each of the lists:\n{genList_6}")

""" Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков """

print()
print('Task 1.5'.center(40, '*'))
print()

genList_7 = [max(genList_1), min(genList_1), max(genList_2), min(genList_2)]
print(f"List containing only the minimum and maximum value of each lists:\n{genList_7}")