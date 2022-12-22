""" Задание 1
Необходимо отсортировать первые две трети списка
в порядке возрастания, если среднее арифметическое
всех элементов больше нуля; иначе — лишь первую треть.
Остальную часть списка не сортировать, а расположить
в обратном порядке. """

print()
print("Task 1".center(40, "*"))
print()

import random


my_list_1 = [random.randint(-10, 10) for _ in range(20)]
avg = int(sum(my_list_1) / len(my_list_1))

if avg > 0:
    cur_len = int(len(my_list_1) / 2)
    result = sorted(my_list_1[:cur_len]) + my_list_1[len(my_list_1):cur_len:-1]
else:
    cur_len = int(len(my_list_1) / 3)
    result = sorted(my_list_1[:cur_len]) + my_list_1[len(my_list_1):cur_len:-1]

print(f"my_list_1 = {my_list_1}\navg = {avg}\nsorted_my_list = {result}")


""" Задание 2
Написать программу «успеваемость». Пользователь
вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
меню для пользователя:
* Вывод оценок (вывод содержимого списка);
* Пересдача экзамена (пользователь вводит номер эле-
мента списка и новую оценку);
* Выходит ли стипендия (стипендия выходит, если
средний бал не ниже 10.7);
* Вывод отсортированного списка оценок: по возрас-
танию или убыванию. """

print()
print("Task 2".center(40, "*"))
print()

grades = list(input("Enter 10 student grades separated by a space:\n").split(" "))
grades = [int(item) for item in grades]

while True:
    options = print("\nPrint grades - Print\nRetaking the exam - Retaking\nScholarship - Sch\nSorted grades - Sort\nStop - Stop")
    choice = input("\nWhat would you like?\n")

    if choice.lower() == "print":
        print()
        for i in range(len(grades) - 1):
            print(f"{i + 1} >> {grades[i]}")
    elif choice.lower() == "retaking":
        retaking = int(input("\nWhich score would you like to change?\n"))
        new_grade = int(input("\nEnter a new grade:\n"))
        grades[retaking - 1] = new_grade
    elif choice.lower() == "sch":
        avg = sum(grades) / len(grades)
        print(f"\nYour average grades = {avg:.1f}\n")
        if avg >= 10.7:
            print("\nYou have a scholarship\n")
        else:
            print("\nYou don't have a scholarship\n")
    elif choice.lower() == "sort":
        sort_choice = input("\nYour choice: A - Ascending, D - descending\n")
        if sort_choice.lower() == "a":
            print(sorted(grades))
        elif sort_choice.lower() == "d":
            print(sorted(grades, reverse=True))
    elif choice.lower() == "stop":
        break
    else:
        print("\nUnknown option\n")


""" Задание 3
Написать программу, реализующую сортировку списка
методом усовершенствованной сортировки пузырьковым
методом. Усовершенствование состоит в том, чтобы ана-
лизировать количество перестановок на каждом шагу, если
это количество равно нулю, то продолжать сортировку
нет смысла — список отсортирован. """

print()
print("Task 3".center(40, "*"))
print()

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        counter_swap = 0
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter_swap += 1
        if counter_swap == 0:
            break

my_list = [random.randint(0, 80) for _ in range(10)]

print(f"Before bubble_sort >> {my_list}")
bubble_sort(my_list)
print(f"After bubble_sort >> {my_list}\n")