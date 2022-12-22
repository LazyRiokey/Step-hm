# Пользователь с клавиатуры вводит значения в список.
# После чего запускаются две потока.
# Первый поток находит максимум в списке.
# Второй поток находит минимум в списке.
# Результаты вычислений выводятся на экран.

import threading

# any_numbers = list(int(input()))
# print(any_numbers)

# def get_max(args):
#     print(f"Max = {max(args)}")


# def get_min(args):
#     print(f"Min = {min(args)}")


# th1 = threading.Thread(target=get_max, args=any_numbers).start()
# th2 = threading.Thread(target=get_min, args=any_numbers).start()

# print(th1)
# print(th2)


# Пользователь с клавиатуры вводит значения в список.
# После чего запускаются две потока.
# Первый поток находит сумму элементов в списке.
# Второй поток находит среднеарифметическое в списке.
# Результаты вычислений выводятся на экран.

# while True:
#     numbers = input("Введите числа через пробел: ")

#     try:
#         numbers = list(map(int, numbers.split()))
#     except ValueError:
#         print("Произошла ошибка!")
#         continue

#     break


# def get_sum(numbers):
#     print(f"Sum = {sum(numbers)}")


# def get_avg(numbers):
#     print(f"Avg = {sum(numbers) / len(numbers)}")


# th1 = threading.Thread(target=get_sum, args=(numbers, )).start()
# th2 = threading.Thread(target=get_avg, args=(numbers, )).start()

# print(th1)
# print(th2)


# Пользователь с клавиатуры вводит путь к файлу,
# содержащему набор чисел. После чего запускаются две потока.
# Первый поток создает новый файл,
# в который запишет только четные элементы списка.
# Второй поток создает новый файл,
# в который запишет только нечетные элементы списка.
# Количество четных и нечетных элементов выводится на экран.


path = input()


def get_file(path):
    with open(path, "r") as file:
        data = file.read()
    return [int(i) for i in data.split(", ")]


def even():
    data = get_file(path)

    with open("even_numbers.txt", "w") as file:
        num = [i for i in data if i % 2 == 0]
        file.write(str(num))
        print(f"Even numbers len: {len(num)}")


def odd():
    data = get_file(path)

    with open("odd_numbers.txt", "w") as file:
        num = [i for i in data if i % 2 != 0]
        file.write(str(num))
        print(f"Odd numbers len: {len(num)}")


th1 = threading.Thread(target=even)
th2 = threading.Thread(target=odd)
th1.start()
th2.start()
