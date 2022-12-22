""" Задание 1:
Пользователь вводит с клавиатуры арифметическое
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция,
число. Возможные операции: +, -,*,/ """

print()
print('Task 1'.center(40, '*'))
print()

try:
    userInput = (input('')).split(' ')
    userInput[0], userInput[2] = int(userInput[0]), int(userInput[2])

    if userInput[1] == '+':
        print(userInput[0] + userInput[2])
    elif userInput[1] == '-':
        print(userInput[0] - userInput[2])
    elif userInput[1] == '*':
        print(userInput[0] * userInput[2])
    elif userInput[1] == '/':
        print(userInput[0] / userInput[2])
except:
    print('Something went wrong!')

""" Задание 2:
В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, 
посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран. """

import random

print()
print('Task 2'.center(40, '*'))
print()

try:
    zeroCounter = 0
    positiveCounter = 0
    negativeCounter = 0
    genList = [random.randint(-100, 100) for i in range(random.randrange(100))]
    maxNum = max(genList)
    minNum = min(genList)

    for i in genList:
        if i > 0:
            positiveCounter += 1
        elif i < 0:
            negativeCounter += 1
        elif i == 0:
            zeroCounter += 1

    print(f"""Your list of numbers: {genList}
    Max >> {maxNum}
    + >> {positiveCounter}
    Min >> {minNum}
    - >> {negativeCounter}
    0 >> {zeroCounter}""")
except:
    print('Something went wrong!')