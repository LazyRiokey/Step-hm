# Пользователь с клавиатуры вводит путь к файлу и слово для поиска.
# После чего запускается поток. Он ищет это слово в файле.
# Результат поиска выводятся на экран.


# import threading


# path = input("Enter the path to the file: ")
# some_information = input("Some information: ")


# def get_file(path):
#     with open(path, "r") as file:
#         return file.read()


# def serch_on_file(information):
#     file = get_file(path=path).split()

#     if information in file:
#         print(f"{information} in file.")
#     else:
#         print("Nothing found...")


# th1 = threading.Thread(target=serch_on_file, args=(some_information,))
# th1.start()
