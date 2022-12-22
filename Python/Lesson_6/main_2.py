""" Задание 1
Есть три кортежа целых чисел необходимо найти
элементы, которые есть во всех кортежах. """

print()
print("Task 1".center(40, "*"))
print()

import random

tuple_1_1 = tuple([random.randint(0, 20) for _ in range(16)])
tuple_1_2 = tuple([random.randint(0, 20) for _ in range(16)])
tuple_1_3 = tuple([random.randint(0, 20) for _ in range(16)])
print(f"tuple_1 = {tuple_1_1}\ntuple_2 = {tuple_1_2}\ntuple_3 = {tuple_1_3}")
print(f"Result = {tuple(set(tuple_1_1) & set(tuple_1_2) & set(tuple_1_3))}")

""" Задание 2
Есть три кортежа целых чисел необходимо найти
элементы, которые уникальны для каждого списка. """

print()
print("Task 2".center(40, "*"))
print()

tuple_2_1 = tuple([random.randint(0, 20) for _ in range(16)])
tuple_2_2 = tuple([random.randint(0, 20) for _ in range(16)])
tuple_2_3 = tuple([random.randint(0, 20) for _ in range(16)])
tuple_2_1, tuple_2_2, tuple_2_3 = tuple(set(tuple_2_1)), tuple(set(tuple_2_2)), tuple(set(tuple_2_3))
result_2 = []

for i in tuple_2_1:
    if i not in tuple_2_2 and i not in tuple_2_3:
        result_2.append(i)

for i in tuple_2_2:
    if i not in tuple_2_1 and i not in tuple_2_3:
        result_2.append(i)

for i in tuple_2_3:
    if i not in tuple_2_2 and i not in tuple_2_1:
        result_2.append(i)

print(f"tuple_2_1 = {tuple_2_1}\ntuple_2_2 = {tuple_2_2}\ntuple_2_3 = {tuple_2_3}")
print(f"result = {result_2}")

""" Задание 3
Есть три кортежа целых чисел необходимо найти эле-
менты, которые есть в каждом из кортежей и находятся
в каждом из кортежей на той же позиции. """

print()
print("Task 3".center(40, "*"))
print()

tuple_3_1 = (0, 1, 16, 22, 14, 35, 18, 19, 22, 7, 6, 0, 44, 28, 14, 13)
tuple_3_2 = (0, 44, 25, 17, 16, 35, 18, 0, 4, 1, -5, 7, 13, 48, 14, 0)
tuple_3_3 = (7, 42, 16, 17, 27, 35, 18, 0, 0, -8, -7, 9, 41, 19, 14, 27)
result_3 = []

for i in range(16):
    if tuple_3_1[i] == tuple_3_2[i] and tuple_3_1[i] == tuple_3_3[i]:
        result_3.append(tuple_3_1[i])

print(f"tuple_3_1 = {tuple_3_1}\ntuple_3_2 = {tuple_3_2}\ntuple_3_3 = {tuple_3_3}")
print(f"result = {result_3}")