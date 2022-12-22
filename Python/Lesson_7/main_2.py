""" Задание 1
Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла. """

print()
print("Task 1".center(40, "*"))
print()

with open("Lesson_7\\file_1.txt", "r", encoding="utf_8") as file_1:
    data_1 = file_1.read().split()

with open("Lesson_7\\file_2.txt", "r", encoding="utf_8") as file_2:
    data_2 = file_2.read().split()

with open("Lesson_7\\file_3.txt", "r", encoding="utf_8") as file_3:
    data_3 = file_3.read().split()

if data_1 == data_2:
    print("file_1 = file_2")

result = []

# Вывел несовпадение в элементах строки.
# Думаю, что так будет нагляднее.
if data_1 != data_3:
    if len(data_1) > len(data_3):
        for i in data_1:
            if i not in data_3:
                result.append(i)
        print(f"file_1 - file_3 = {result}")
    else:
        for j in data_3:
            if j not in data_1:
                result.append(j)
        print(f"file_3 - file_1 = {result}")


""" Задание 2
Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному
файлу:
* Количество символов;
* Количество строк;
* Количество гласных букв;
* Количество согласных букв;
* Количество цифр. """

print()
print("Task 2".center(40, "*"))
print()

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
numbers = "0123456789"
vowels_counter = 0
consonants_counter = 0
num_counter = 0
paragraph_counter = 1
symbol_counter = 0

with open("Lesson_7\\file_4.txt", "r", encoding="utf_8") as file_4:
    data_4 = file_4.read()

with open("Lesson_7\\file_5.txt", "w", encoding="utf_8") as file_5:

    for i in data_4:
        symbol_counter += 1
        if i.lower() in vowels:
            vowels_counter += 1
        elif i.lower() in consonants:
            consonants_counter += 1
        elif i in numbers:
            num_counter += 1
        elif i == "\n":
            paragraph_counter += 1

    file_5.write(f"Symbol counter = {symbol_counter}\n")
    file_5.write(f"Paragraph counter = {paragraph_counter}\n")
    file_5.write(f"Vowels counter = {vowels_counter}\n")
    file_5.write(f"Consonants counter = {consonants_counter}\n")
    file_5.write(f"Numbers counter = {num_counter}")

with open("Lesson_7\\file_5.txt", "r", encoding="utf_8") as file_5:
    data_5 = file_5.read()
    print(data_5)


""" Задание 3
Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл. """

print()
print("Task 3".center(40, "*"))
print()

with open("Lesson_7\\file_6.txt", "r+", encoding="utf_8") as file_6:
    data_6 = file_6.readlines()
    pop_string = data_6.pop()

with open("Lesson_7\\file_6.txt", "w", encoding="utf_8") as file_6:
    for line in data_6:
        file_6.write(str(line))

with open("Lesson_7\\file_7.txt", "w", encoding="utf_8") as file_7:
    file_7.write(pop_string)


""" Задание 4
Дан текстовый файл. Найти длину самой длинной
строки. """

print()
print("Task 4".center(40, "*"))
print()

with open("Lesson_7\\file_6.txt", "r+", encoding="utf_8") as file_6:
    data_7 = file_6.readlines()
    print(len(max(data_7)))


""" Задание 5
Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово. """

print()
print("Task 5".center(40, "*"))
print()

user_inpur = input("Enter the search word: ").lower()

with open("Lesson_7\\file_6.txt", "r+", encoding="utf_8") as file_6:
    data_8 = file_6.read().lower()
    print(f"The word \"{user_inpur}\" occurs {data_8.count(user_inpur)} times in the text.")

""" Задание 6
Дан текстовый файл. Найти и заменить в нем задан-
ное слово. Что искать и на что заменять определяется
пользователем. """

print()
print("Task 6".center(40, "*"))
print()

search_word = input("Enter the search word: ")
replaced_word = str(input("Enter the replaced word: "))

with open("Lesson_7\\file_8.txt", "r+", encoding="utf_8") as file_8:
    data_9 = file_8.read()
    new_data = data_9.replace(search_word, replaced_word)

with open("Lesson_7\\file_8.txt", "r+", encoding="utf_8") as file_8:
    file_8.write(new_data)