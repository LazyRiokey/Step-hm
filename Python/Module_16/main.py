""" Задание 1
При старте приложения запускаются три потока.
Первый поток заполняет список случайными числами.
Два других потока ожидают заполнения. Когда список
заполнен оба потока запускаются. Первый поток находит
сумму элементов списка, второй поток среднеарифмети-
ческое значение в списке. Полученный список, сумма и
среднеарифметическое выводятся на экран. """


import random
import threading

# numbers = []

# def set_rand_numbers(l: int):
#     for _ in range(l):
#         numbers.append(random.randint(1, 100))

#     print(f'Список случайных чисел:\n{numbers}')


# def get_sum(list_of_numbers: list):
#     print(f'Сумма элементов списка: {sum(list_of_numbers)}')


# def get_arithmetic_mean(list_of_numbers: list):
#     print(f'Среднеарифметическое элементов списка: {sum(list_of_numbers) / len(list_of_numbers)}')


# th1 = threading.Thread(target=set_rand_numbers, args=(10, ))
# th2 = threading.Thread(target=get_sum, args=(numbers, ))
# th3 = threading.Thread(target=get_arithmetic_mean, args=(numbers, ))

# th1.start()
# th1.join()
# th2.start()
# th3.start()


""" Задание 2
Пользователь с клавиатуры вводит путь к файлу.
После чего запускаются три потока. Первый поток за-
полняет файл случайными числами. Два других потока
ожидают заполнения. Когда файл заполнен оба потока
стартуют. Первый поток находит все простые числа, вто-
рой поток факториал каждого числа в файле. Результаты
поиска каждый поток должен записать в новый файл. На
экран необходимо отобразить статистику выполненных
операций. """


from math import factorial
from sympy import isprime


# my_path = str(input("Enter path on file: "))


# def set_rand_num_on_file():
#     with open(file=my_path, mode="w", encoding="UTF-8") as file:
#         for i in range(10):
#             if i != 9:
#                 file.write(str(random.randint(1, 100)) + ", ")
#             else:
#                 file.write(str(random.randint(1, 100)))

#         print(f'Файл "{my_path}" сформирован. Значения записаны.')


# def calc_isPrime():
#     with open(file="file.txt", mode="r", encoding="UTF-8") as file:
#         numbers = file.read()
#         my_list = [int(i) for i in numbers.split(", ")]
#         prime_numbers = []
#         for i in my_list:
#             if isprime(i):
#                 prime_numbers.append(i)
#         print(f"Список простых чисел сформирован.")

#         with open(file="prime_numbers.txt", mode="w", encoding="UTF-8") as file:
#             file.write(str(prime_numbers))
#             print(f'Простые числа записаны в файл "{file.name}".')


# def calc_factorial():
#     with open(file="file.txt", mode="r", encoding="UTF-8") as file:
#         numbers = file.read()
#         my_list = [int(i) for i in numbers.split(", ")]
#         fact_nums = [factorial(i) for i in my_list]
#         print("Факториал каждого числа вычислен.")

#     with open(file="factorials.txt", mode="w", encoding="UTF-8") as file:
#         for i in range(len(my_list)):
#             file.write(f"{str(my_list[i])} > {str(fact_nums[i])}\n")
#         print(f'Значения записаны в файл "{file.name}".')


# th1 = threading.Thread(target=set_rand_num_on_file)
# th2 = threading.Thread(target=calc_isPrime)
# th3 = threading.Thread(target=calc_factorial)

# th1.start()
# th1.join()
# th2.start()
# th3.start()


""" Задание 3
Пользователь с клавиатуры вводит путь к существу-
ющей директории и к новой директории. После чего
запускается поток, который должен скопировать содер-
жимое директории в новое место. Необходимо сохранить
структуру директории. На экран необходимо отобразить
статистику выполненных операций. """


import shutil


# def dir_coppy():
#     from_directory = input("From directory: ")
#     to_directory = input("To directory: ")
#     shutil.copytree(src=from_directory, dst=to_directory)
#     print(f"Копирование директории {from_directory} в директорию {to_directory} - завершено!")


# th1 = threading.Thread(target=dir_coppy)

# th1.start()


""" Задание 4
Пользователь с клавиатуры вводит путь к существующей
директории и слово для поиска. После чего запускаются
два потока. Первый должен найти файлы, содержащие
искомое слово и слить их содержимое в один файл. Вто-
рой поток ожидает завершения работы первого потока.
После чего проводит вырезание всех запрещенных слов
(список этих слов нужно считать из файла с запрещенны-
ми словами) из полученного файла. На экран необходимо
отобразить статистику выполненных операций. """


# Очень не уверен в реализации данной задачи...
# Периодически "слетает" разметка текста в файле.

import os
import re

# FORBIDEN_WORDS = "task_4\\forbidden_words.txt"
# BEFORE_CUT = "task_4\\result_before_cut.txt"
# AFTER_CUT = "task_4\\result_after_cut.txt"


# def search_word():
#     exist_dir = input("Enter exist directory: ")
#     search_word = input("Enter the search word: ").lower()
#     files = os.listdir(exist_dir)

#     for i in files:
#         with open(file=f"{exist_dir}/{i}", mode="r", encoding="UTF-8") as file:
#             some_text = file.read()
#             if search_word in some_text.lower():
#                 with open(file=BEFORE_CUT, mode="a", encoding="UTF-8") as file:
#                     file.write(some_text)

#     print(
#         f'Найдены файлы, содержащие искомое слово - {search_word}\nи слиты в один файл по пути - "BEFORE_CUT"'
#     )


# def cut_words():
#     with open(file=FORBIDEN_WORDS, mode="r", encoding="UTF-8") as file:
#         f_words = file.readlines()
#         for counter, word in enumerate(f_words):
#             f_words[counter] = word.replace("\n", "")

#         print('Извлечён список запрещённых слов из файла - "FORBIDEN_WORDS"')

#     with open(file=BEFORE_CUT, mode="r", encoding="UTF-8") as file:
#         some_text = re.split(r"[ \t\v\r\f]", file.read())
#         print("Текст разбит на отдельные слова.")

#         for word in some_text:
#             if re.sub(r"[\W_]", "", word.lower()) in f_words:
#                 some_text.remove(word)

#         print('В тексте удалены слова, которые находятся в файле "FORBIDEN_WORDS"')

#         some_text = " ".join(some_text)

#         print("Текст пересобран.")
#         save_after_cut(some_text)


# def save_after_cut(text):
#     with open(file=AFTER_CUT, mode="w", encoding="UTF-8") as file:
#         file.write(text)
#         print('Текст с удалёнными словами записан в файл по пути "AFTER_CUT"')


# th1 = threading.Thread(target=search_word)
# th2 = threading.Thread(target=cut_words)

# th1.start()
# th1.join()
# th2.start()
