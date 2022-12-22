""" Задание 1
Напишите информационную систему «Сотрудники». 
Программа должна обеспечивать ввод данных, редакти-
рование данных сотрудника, удаление сотрудника, поиск 
сотрудника по фамилии, вывод информации обо всех 
сотрудниках, указанного возраста, или фамилия которых 
начинается на указанную букву. Организуйте возможность 
сохранения найденной информации в файл. Также весь 
список сотрудников сохраняется в файл (при выходе из 
программы — автоматически, в процессе исполнения 
программы — по команде пользователя). При старте 
программы происходит загрузка списка сотрудников из 
указанного пользователем файла. """

import modules.my_functions as func
from copy import copy


path = func.get_dir()
while True:

    print()
    func.greeting()
    choice = input('Введите номер необходимой операции: ')
    
    if choice == '1':
        print()
        employee = func.enter_employee().split()
        while True:
            choice = input(f'\n{employee}\nВсё верно? - ').lower()
            if choice == 'да':
                func.add_employee(path, " ".join(employee))
                break
            elif choice == 'нет':
                print('Где именно произошла ошибка?')
                print('\'1\' - Фамилия\n\'2\' - Имя\n\'3\' - Отчество\n\'4\' - Возраст')
                choice = input()
                if choice == '1':
                    employee[0] = input('Укажите фамилию сотрудника: ')
                elif choice == '2':
                    employee[1] = input('Укажите имя сотрудника: ')
                elif choice == '3':
                    employee[2] = input('Укажите отчество сотрудника: ')
                elif choice == '4':
                    employee[3] = input('Укажите возраст сотрудника: ')

    elif choice == '2':
        print()
        choice = input('Введите фамилию сотрудника для его редактирования: ')
        result = func.surname_employee(path, choice)

        if result == None:
            print(f'Сотрудника с фамилией {choice} не существует!')
        else:
            new_result = copy(result).split(' ')
            print(result)
            print()
            while True:
                print('\nЧто Вы хотите изменить?\n')
                print('\'1\' - Фамилия\n\'2\' - Имя\n\'3\' - Отчество\n\'4\' - Возраст\n\'5\' - Подтвердить изменения')
                choice = input()
                if choice == '1':
                    new_result[0] = input('Введите новую фамилию сотрудника: ')
                elif choice == '2':
                    new_result[1] = input('Введите новое имя сотрудника: ')
                elif choice == '3':
                    new_result[2] = input('Введите новое отчество сотрудника: ')
                elif choice == '4':
                    new_result[3] = input('Введите новый возраст сотрудника: ')
                elif choice == '5':
                    func.editing_employee(path, result, new_result)
                    break
                print(*new_result)

    elif choice == '3':
        while True:
            print()
            choice = input('Введите фамилию сотрудника для его удаления: ')
            employee = ''.join(func.surname_employee(path, choice))
            print(employee)
            choice = input('Вы желаете удалить данного сотрудника? ').lower()
            if choice == 'да':
                func.del_employee(path, employee)
                break
            elif choice == 'нет':
                continue
            else:
                print('Вариант ответа может быть только "да" или "нет"!\n')
                continue
    
    elif choice == '4':
        choice = input('Как именно производить поиск?\n1 - по фамилиям\n2 - по возрасту\n')
        print()
        data = func.search(path, choice)
        new_path = path[0: -4] + "_copy.txt"

        if choice == '1':
            with open(new_path, 'a+', encoding='utf_8') as save_copy:
                save_copy.write(f'Результат поиска сотрудников по фамилии:\n\n')
                save_copy.writelines(data)
        elif choice == '2':
            with open(new_path, 'a+', encoding='utf_8') as save_copy:
                save_copy.write('Результат поиска сотрудников по возрасту:\n\n')
                save_copy.writelines(data)
                
    elif choice == '5':
        func.print_employees(path)
    
    elif choice == '6':
        break
    
    else:
        print('Некорректный ввод!\n')
        continue