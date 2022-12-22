""" Задание 1
Пользователь вводит с клавиатуры три цифры. Необ-
ходимо создать число, содержащее эти цифры. Например,
если с клавиатуры введено 1, 5, 7, тогда нужно сформи-
ровать число 157. """

print()
print("Task 1".center(40, "*"))
print()

try:
    someNumbers = input('Enter some numbers: ')
    listOfNumbers = []

    for i in someNumbers:
        if i.isdigit():
            listOfNumbers.append(i)
    strNumbers = "".join(listOfNumbers)
    print(strNumbers)
except Exception:
    print('Something went wrong...')

""" Задание 2
Пользователь вводит с клавиатуры число, состоящее
из четырех цифр. Требуется найти произведение цифр.
Например, если с клавиатуры введено 1324, тогда резуль-
тат произведения 1*3*2*4 = 24. """

print()
print("Task 2".center(40, "*"))
print()

try:
    userInput = input('Enter a number consisting of four numbers: ')
    result = 1

    for i in userInput:
        if int(i) == 0:
            raise ZeroDivisionError
        result *= int(i)
    print(f'The product of numbers {userInput} is equal to {result}')
except ZeroDivisionError:
    print("Can't multiply by 0")
except Exception:
    print('Something went wrong...')

""" Задание 3
Пользователь вводит с клавиатуры количество метров.
Требуется вывести результат перевода метров в сантиме-
тры, дециметры, миллиметры, мили. """

print()
print("Task 3".center(40, "*"))
print()

try:
    meters = int(input('Enter the number of meters: '))
    cm = meters * 100
    dm = meters * 10
    mm = meters * 1000
    mi = meters / 1609

    print(f'{meters} meters equals:\ncm = {cm}\ndm = {dm}\nmm = {mm}\nmi = {mi}')
except Exception:
    print('Something went wrong...')

""" Задание 4
Напишите программу, вычисляющую площадь тре-
угольника. Пользователь с клавиатуры вводит размер
основания треугольника и размер высоты. """

print()
print("Task 4".center(40, "*"))
print()

try:
    a = int(input('Enter the base of the triangle: '))
    h = int(input('Enter the height of the triangle: '))
    s = 0.5 * a * h

    print(f'The area of a triangle with base {a} and height {h} is {s}')
except Exception:
    print('Something went wrong...')

""" Задание 5
Пользователь с клавиатуры вводит четырёхзначное
число. Необходимо перевернуть число и отобразить
результат. Например, если введено 4512, результат 2154. """

print()
print("Task 5".center(40, "*"))
print()

try:
    userNumber = list(input('Enter a four-digit number: '))

    if len(userNumber) > 4 or len(userNumber) < 4:
        raise Exception
    result = ''.join(userNumber[::-1])
    print(f'Reversed number is {result}')
except Exception:
    print('Something went wrong...')

""" Или """

# try:
#     userNumber = input('Enter a four-digit number:')
#     counter = len(userNumber) - 1
#     result = ""

#     if len(userNumber) > 4 or len(userNumber) < 4:
#         raise Exception
    
#     while counter >= 0:
#         result += userNumber[counter]
#         counter -= 1

#     print(f'Reversed number is {result}')
# except Exception:
#     print('Something went wrong...')