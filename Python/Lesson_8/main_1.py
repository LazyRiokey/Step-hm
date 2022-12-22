""" Задача 1 """

def is_divisible_by_6(number):
    lst_number = list(str(abs(number)))
    numbers = list(map(int, lst_number))
    sum_numbers = sum(numbers)

    if (sum_numbers % 3 == 0) and (numbers[-1] % 2 == 0):
        print(f'Чило {number} делится на 6')
    else:
        print(f'Чило {number} неделимо')

is_divisible_by_6(121)

""" Задача 2 """

def list_sort(lst):
    print(sorted(lst, key=abs, reverse=True))

list_sort([1, 0, -5, -3, 8, 9])

""" Задача 3 """

def all_eq(lst):
    max_lst_len = len(max(lst, key=len))
    return ([x.ljust(max_lst_len, '_') for x in lst])

print(all_eq(['asdf', 'a', 'urjernsh', 'zzx']))

""" Задача 4 """

def sieve(lst):
    return tuple(sorted(set(lst), reverse=True))

my_list = [11, 555, 16, 7, 14, 224, 96, 17, 14, 7, 74, 11]
print(sieve(my_list))

""" Задача 5 """

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
print(dictionary_1 | dictionary_2)

""" Задача 6 """

my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
result_6 = 1

for i in my_dictionary.values():
    result_6 *= i

print(result_6)

""" Задача 7 """

my_lst_1 = ['a', 'b', 'c', 'd']
my_lst_2 = [1, 2, 3, 4]
result_7 = dict(zip(my_lst_1, my_lst_2))
print(result_7)

""" Задача 8 """

my_str = 'pythonist'
my_dict = {i: my_str.count(i) for i in my_str}
print(my_dict)

""" Задача 9 """

def more_than_five(lst):
    return [i for i in my_list_9 if abs(i) > 5 ]

my_list_9 = [1, 22, 5, 6, 4, 3, -15, 7, 0, -33]
print(more_than_five(my_list_9))


""" Задача 10 """

def get_alphabet():
    rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    aggregate = '^' * 27
    counter = 0

    for i in rus_lower:
        counter += 1
        if counter % 3 == 0:
            print(f'| {i.capitalize()} {i} |', end='')
            print(f'\n{aggregate}')
        else:
            print(f'| {i.capitalize()} {i} |', end='')

get_alphabet()

""" Задача 11 """

import re

def check(string):
    regexp = r'^[a-zA-Z0-9]*$'
    result = re.match(regexp, string)
    
    if result is not None:
        return True
    else:
        return False

test_str_1 = 'ASDcsadfg'
test_str_2 = 'ASDcs!@adfg123!!@#'

print(check(test_str_1))
print(check(test_str_2))