# text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.""".lower().split()
# result = [i for i in text if i.startswith('b')]
# print(result)

# import re

# text = "A, very very; irregular_sentence!"
# result = re.sub(r'[^\w\s]','', text)
# print(result)

# myList = [12, 3, 5, 2, 4, 8]
# sumResult = 0
# multResult = 1

# for i in myList:
#     sumResult += i
#     multResult *= i

# print(f'Sum >> {sumResult}\nMult >> {multResult}')

# print([i for i in range(0, 91) if i % 2 == 0])

# myList = [i for i in range(2, 93)]
# mapped = list(filter(lambda x: x % 2 == 0, myList))
# print(mapped)

# Сортировка методом пузырька
# def list_sort(lst):
#     for i in range(len(lst)):
#         for k in range(0, len(lst) - i - 1):
#             if lst[k] < lst[k + 1]:
#                 tmp = lst[k]
#                 lst[k] = lst[k + 1]
#                 lst[k + 1] = tmp

# myList = [8, 15, -5, 0, 17, 26, 3]
# list_sort(myList)
# print(myList)

# from random import randint

# def game(start, stop):

#     counter = 0
#     number = randint(start, stop)

#     while True:
#         myChoice = int(input("Ваш вариант? - "))
#         counter += 1

#         if number > myChoice:
#             print ("Искомое число больше")
#         elif number < myChoice:
#             print ("Искомое число меньше")
#         else:
#             print (f"Вы угадали число {number} за {counter} попыток ")
#             break

# game(0, 10)