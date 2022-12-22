""" Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates """

print()
print('Task 1'.center(40, '*'))
print()

def format_text():
    print(f"“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\n\t\t\t\t\tBill Gates")

format_text()


""" Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними. """

print()
print('Task 2'.center(40, '*'))
print()

def print_even(start, stop):
    tmp = [i for i in range(start, stop + 1) if i % 2 == 0]
    print(*tmp)

print_even(2, 10)


""" Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны ква-
драта, символ и переменную логического типа:
- если она равна True, квадрат заполненный;
- если False, квадрат пустой. """

print()
print('Task 3'.center(40, '*'))
print()

def draw_square(side,simbol,bool):
    hLine = (simbol + ' ') * side

    if bool:
        iLine = hLine
    else:
        iLine = simbol + " " * (side + (side - 3)) + simbol
    print(hLine)

    for _ in range(side - 2):
        print(iLine)
    print(hLine)
    
draw_square(6,"#",False)
print("")
draw_square(6,"#",True)


""" Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров. """

print()
print('Task 4'.center(40, '*'))
print()

def print_min(*args):
    result = args[0]

    for i in args:
        if result < i:
            continue
        else:
            result = i
    
    print(result)

# Или

# def print_min(*args):
#     print(min(args))

print_min(-5, 14, 0, 2, -6)


""" Задание 5
Напишите функцию, которая возвращает произве-
дение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапа-
зона перепутаны (например, 5 — верхняя граница, 25 —
нижняя граница), их нужно поменять местами. """

print()
print('Task 5'.center(40, '*'))
print()

def get_multiplication(start_range, stop_range):
    if start_range > stop_range:
        start_range, stop_range = stop_range, start_range
    
    result = 1
    
    for i in range(start_range, stop_range + 1):
        if result == 0:
            print(result)
            break
        else:
            result *= i
    
    print(result)

get_multiplication(5, 1)


""" Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4. """

print()
print('Task 6'.center(40, '*'))
print()

def get_numbers(number):
    print(len(str(number)))

# Или

# def get_numbers(number):
#     number = str(number)
#     counter = 0

#     for _ in number:
#         counter += 1
    
#     print(counter)

get_numbers(3456)


""" Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве пара-
метра. Если число палиндром нужно вернуть из функции
true, иначе false. """

print()
print('Task 7'.center(40, '*'))
print()

def is_palindrome(palindrome):
    if str(palindrome).lower() == str(palindrome).lower()[::-1]:
        return True
    else:
        return False

palindrome = '12321'
print(is_palindrome(palindrome))