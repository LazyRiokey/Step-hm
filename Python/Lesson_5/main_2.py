""" Задание 1
Напишите функцию, вычисляющую произведение
элементов списка целых. Список передаётся в качестве па-
раметра. Полученный результат возвращается из функции. """

print()
print('Task 1'.center(40, '*'))
print()

def get_multiply(list):
    try:
        result = 1

        for elem in list:
            if elem != 0:
                result *= elem
    
        return result
    except Exception:
        print('Something went wrong!')

x = [1, 2, 3, 4, 5]
print(get_multiply(x))


""" Задание 2
Напишите функцию для нахождения минимума в
списке целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции. """

print()
print('Task 2'.center(40, '*'))
print()

def get_min(list):
    return [min(list)]

y = [10, -5, 26, 1, 0]
print(get_min(y))


""" Задание 3
Напишите функцию, определяющую количество про-
стых чисел в списке целых. Список передаётся в качестве
параметра. Полученный результат возвращается из функции. """

print()
print('Task 3'.center(40, '*'))
print()

# Более чем уверен, что есть алгоритмы,
# которые выполняются куда быстрее написанного.

def is_prime(list):
    result = []

    for elem in list:
        if elem < 2:
            continue
        elif all(elem % i != 0 for i in range(2, int(elem ** 0.5) + 1)):
            result.append(elem)
    
    return result

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(is_prime(test_list))


""" Задание 4
Напишите функцию, удаляющую из списка целых
некоторое заданное число. Из функции нужно вернуть
количество удаленных элементов. """

print()
print('Task 4'.center(40, '*'))
print()

def remove_number(list, remove_elem):
    new_list = []

    for i in list:
        if i == remove_elem:
            new_list.append(list.pop(list.index(i)))
        else:
            continue
    
    return new_list

my_list = [10, -5, 26, 1, 0, 10, 17, 11]
print(remove_number(my_list, 10))


""" Задание 5
Напишите функцию, которая получает два списка в
качестве параметра и возвращает список, содержащий
элементы обоих списков. """

print()
print('Task 5'.center(40, '*'))
print()

def get_total_list(list_1, list_2):
    return list_1 + list_2

list_1 = [1, 2, 3, 4]
list_2 = [1, 5, 8, 0]
total_list = get_total_list(list_1, list_2)
print(total_list)


""" Задание 6
Напишите функцию, высчитывающую степень каждого
элемента списка целых. Значение для степени передаётся
в качестве параметра, список тоже передаётся в качестве
параметра. Функция возвращает новый список, содержа-
щий полученные результаты. """

print()
print('Task 6'.center(40, '*'))
print()

def list_pow(list, degree):
    new_list = []

    for i in list:
        new_list.append(pow(i, degree))
    
    return new_list

my_list_2 = [1, 2, 3, 4, 5]
result_2 = list_pow(my_list_2, 3)
print(result_2)