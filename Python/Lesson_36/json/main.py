import json
import pickle



# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).


# countries = {
#     "Польша": "Варшава",
#     "Чехия": "Прага",
#     "Великобритания": "Лондон",
#     "Германия": "Берлин",
# }


# def add_countrie(countrie, capital):
#     countries[countrie] = capital
#     print(f"{countrie} : {capital} was add in dict 'countries'.")

# def search_capital(countrie):
#     item = countries.get(countrie)
#     if item != None:
#         print(f"{countrie} : {item}")
#         return item
#     else:
#         print(f"{countrie} is not in the dictionary.")

# def del_countrie(countrie):
#     if search_capital(countrie) != None:
#         pop_item = countries.pop(countrie)
#         print(f"{countrie} : {pop_item} was del in dict 'countries'.")

# def corr_countrie(countrie):
#     if search_capital(countrie) != None:
#         countries[countrie] = input("Enter new capital: ")

# def write_pickle(dict, filename):
#     with open(filename, 'wb') as f:
#         pickle.dump(dict, f)

# def open_pickle(filename):
#     with open(filename, 'rb') as f:
#         new_dict = pickle.load(f)
#         return new_dict



# -----------------
# Создайте класс «Самолет». Наполните его необходимыми характеристиками и методами. Реализуйте упаковку и
# распаковку объектов класса «Самолет» с использованием
# модуля pickle


# class Plane:
#     def __init__(self, wheels:int, wings:int, engines:int):
#         self.wheels = wheels
#         self.wings = wings
#         self.engines = engines
    
#     def fly(self):
#         pass

#     def takeoff(self):
#         pass

#     def landing(self):
#         pass

# my_plane = Plane(3, 2, 3)

# with open('plane.pickle', 'wb') as f:
#     pickle.dump(my_plane, f)

# with open('plane.pickle', 'rb') as f:
#     new_class = pickle.load(f)

# print(new_class)


# Добавьте к заданию 1 возможность упаковки/распаковки с использованием модуля json.



# countries = {
#     "Польша": "Варшава",
#     "Чехия": "Прага",
#     "Великобритания": "Лондон",
#     "Германия": "Берлин",
# }


# def add_countrie(countrie, capital):
#     countries[countrie] = capital
#     print(f"{countrie} : {capital} was add in dict 'countries'.")

# def search_capital(countrie):
#     item = countries.get(countrie)
#     if item != None:
#         print(f"{countrie} : {item}")
#         return item
#     else:
#         print(f"{countrie} is not in the dictionary.")

# def del_countrie(countrie):
#     if search_capital(countrie) != None:
#         pop_item = countries.pop(countrie)
#         print(f"{countrie} : {pop_item} was del in dict 'countries'.")

# def corr_countrie(countrie):
#     if search_capital(countrie) != None:
#         countries[countrie] = input("Enter new capital: ")

# def write_file(dict, filename):
#     choice = input('Json or pickle? ')
#     if choice.lower() == 'json':
#         with open(filename + '.json', 'w') as f:
#             json.dump(dict)
#     else:
#         with open(filename + '.pickle', 'wb') as f:
#             pickle.dump(dict, f)

# def open_file(filename):
#     choice = input('Json or pickle? ')
#     if choice.lower() == 'json':
#         with open(filename + '.json', 'r') as f:
#             json.load(f)
#     else:
#         with open(filename, 'rb') as f:
#             new_dict = pickle.load(f)
#             return new_dict



def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class Plane:
    pass

a = Plane()
b = Plane()

print(a, b)


# Паттерн фабрика

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def calc_risks(self):
        pass

class Worker(Product):
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours
    
    def calc_risks(self):
        return 100 / self.hours

    def __str__(self):
        return f"{self.name}, {self.age}, {self.hours}"

class Unemployeed(Product):
        def __init__(self, name, age, able):
            self.name = name
            self.age = age
            self.able = able
    
        def calc_risks(self):
            if self.able:
                return self.age + 10
            else:
                return self.age + 30

        def __str__(self):
            return f"{self.name}, {self.age}, {self.able}"


class Factory:
    def get_person(self, type_person):
        if type_person == 'worker':
            return Worker('Ivan', 35, 40)
        elif type_person == 'unemployeed':
            return Unemployeed('Oleg', 40, False)


f = Factory()

p1 = f.get_person('worker')
p2 = f.get_person('unemployeed')

print(p1)
print(p2)