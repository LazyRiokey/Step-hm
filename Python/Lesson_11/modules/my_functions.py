""" Импорт библиотек """
import sys
import os


""" Открытие файла """

def get_dir():
    empl_dir = sys.path[0] + '\\files\\'
    list_empl = os.listdir(empl_dir)
    print('\nСписок файлов:\n')
    for n, item in enumerate(list_empl):
        print(f'{n + 1}. {item}')
    choice = int(input('Введите номер файла, который Вы хотите открыть: '))
    return empl_dir + list_empl[choice - 1]

""" Приветствие """

def greeting():
    print('База \'Сотрудники\''.center(40, '*'),'\n')
    print('\'1\' для Добавления сотрудника.')
    print('\'2\' для Редактирования записи о сотруднике.')
    print('\'3\' для Удаления сотрудника')
    print('\'4\' для Поиска сотрудника(ов)')
    print('\'5\' для Вывода информации о сотрудниках')
    print('\'6\' для Выхода из \'программы\'\n')

""" Добавление сотрудника """

# Ввод данных сотрудника и сбор в строку
def enter_employee():
    surname = input('Укажите фамилию сотрудника: ')
    name = input('Укажите имя сотрудника: ')
    patronymic = input('Укажите отчество сотрудника: ')
    age = input('Укажите возраст сотрудника: ')
    return surname + ' ' + name + ' ' + patronymic + ' ' + age

# Запись сотрудника в конец файла
def add_employee(path, new_employee):
    with open(path, 'a', encoding='utf_8') as employees:
        employees.write('\n')
        employees.write(new_employee)

""" Редактирование сотрадника """

# Поиск по фамилии
def surname_employee(path, surname):
    with open(path, 'r', encoding='utf_8') as employees:
        data = employees.readlines()
        for _, item in enumerate(data):
            if surname in item:
                return item

        return None

# Перезапись сотрудника
def editing_employee(path, old_employee, new_employee):
    with open(path, 'r', encoding='utf_8') as employees:
        data = employees.readlines()

        for n, item in enumerate(data):
            if old_employee in item:
                data[n] = ' '.join(new_employee)
                break
                    

    with open(path, 'w', encoding='utf_8') as employees:
        employees.writelines(data)


""" Вывод списка сотрудников на экран """
def print_employees(path):
    with open(path, 'r', encoding='utf_8') as employees:
        data = employees.read()
        print(data)

""" Удаление сотрудника """

def del_employee(path, employee):
    with open(path, 'r', encoding='utf_8') as employees:
        data = employees.readlines()

        for n, item in enumerate(data):
            if employee in item:
                data.remove(str(data[n]))
                break

    with open(path, 'w', encoding='utf_8') as employees:
        employees.writelines(data)

""" Поиск всех сотрудников по фамилии или возрасту """

def search(path, choice):
    with open(path, 'r', encoding='utf_8') as employees:
        data = employees.readlines()
        result = []
        if choice == '1':
            surname = input('Введите букву, на которую должны начинаться фамилии сотрудников: ')
            print("Список сотрудников: ")
            for n, item in enumerate(data):
                if data[n][0] == surname.upper():
                    result.append(item)

            if len(result) == 0:
                print(f'Сотрудников с фамилией на букву "{surname}" в компании нет!')
            else:
                print(*result)

            
        elif choice == '2':
            age = input('Введите возраст сотрудников, которых Вы хотите увидеть: ')
            print("Список сотрудников: ")
            for n, item in enumerate(data):
                if item.split(" ")[3] == age:
                    result.append(item)
            
            if len(result) == 0:
                print(f'Сотрудников с возрастом {age} в компании нет!')
            else:
                print(*result)   

    return result