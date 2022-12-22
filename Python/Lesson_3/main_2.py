""" Задание 1
Пользователь вводит с клавиатуры три числа. В за-
висимости от выбора пользователя программа выводит
на экран сумму трёх чисел или произведение трёх чисел. """

print()
print("Task 1".center(40, "*"))
print()

try:
    userInput = input("Enter 3 numbers separated by a space: ").split(" ")

    if len(userInput) < 3:
        raise Exception
    
    answer = input("Calculate the sum or product of numbers\nS = sum\nP = product\nYour answer: ")
    result = int()
    
    if answer.lower() == 's':
        result = 0
        for i in userInput:
            result += int(i)
        print(f"The sum of the numbers {userInput} is {result}")
    elif answer.lower() == 'p':
        result = 1
        for i in userInput:
            if int(i) == 0:
                raise ZeroDivisionError
            else:
                result *= int(i)
        print(f"The product of the numbers {userInput} is {result}")
    else:
        raise Exception
except ZeroDivisionError:
    print("Can't multiply by 0")
except Exception:
    print("Something went wrong...")

""" Задание 2
Пользователь вводит с клавиатуры три числа. В за-
висимости от выбора пользователя программа выводит
на экран максимум из трёх, минимум из трёх или сред-
неарифметическое трёх чисел. """

print()
print("Task 2".center(40, "*"))
print()

try:
    userInput = input("Enter 3 numbers separated by a space: ").split(" ")
    
    if len(userInput) < 3:
        raise Exception
    
    answer = input("Calculate the Max, Min or Average of numbers\nmax = Max\nmin = Min\navg = Average\nYour answer: ")
    result = int()


    if answer.lower() == "max":
        result = max(userInput)
        # Или
        # result = int(userInput[0])
        # for i in userInput:
        #     if result < int(i):
        #         result = int(i)
        print(f"Of the numbers {userInput} the maximum is {result}")
    elif answer.lower() == "min":
        result = min(userInput)
        # Или
        # result = int(userInput[0])
        # for i in userInput:
        #     if result > int(i):
        #         result = int(i)
        print(f"Of the numbers {userInput} the minimum is {result}")
    elif answer.lower() == "avg":
        for i in userInput:
            result += int(i)
        result /= len(userInput)
        print(f"Of the numbers {userInput} the average is {result}")
    else:
        raise Exception
except Exception:
    print("Something went wrong...")

""" Задание 3
Пользователь вводит с клавиатуры количество ме-
тров. В зависимости от выбора пользователя программа
переводит метры в мили, дюймы или ярды. """

print()
print("Task 3".center(40, "*"))
print()

try:
    meters = int(input('Enter the number of meters: '))

    if meters < 0:
        raise Exception
    
    answer = input("Convert meters to inches, miles or yards\ni = Inches\nmi = Miles\ny = Yards\nYour answer: ")
    result = int()

    if answer.lower() == 'i':
        result = meters * 39.37
        print(f'{meters} meters equals {result} inches')
    elif answer.lower() == 'mi':
        result = meters / 1609
        print(f'{meters} meters equals {result} miles')
    elif answer.lower() == 'y':
        result = meters * 1.094
        print(f'{meters} meters equals {result} yards')
    else:
        raise Exception
except Exception:
    print("Something went wrong...")