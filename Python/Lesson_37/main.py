# Пользователь вводит с клавиатуры набор чисел и путь
# к файлу для сохранения полученных данных. Необходимо:
# ■ Сохранить все полученные числа.
# ■ Найти максимум, минимум. Эти значения сохранить
# в том же файле.
# ■ Отобразить числа.
# ■ Отобразить максимум и минимум.
# ■ Создать класс для логгирования операций. При создании объекта класса нужно уточнить куда производится
# логгирование: экран или файл. В программе можно
# создать только один объект класса. Все действия
# в программе необходимо логгировать с помощью
# объекта этого класса.


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


# Адаптер

# Американская вилка
class UsaFork:
    def power_usa(self):
        print("power on. Usa")


# Европейская вилка
class EuroFork:
    def power_euro(self):
        print("power on. Euro")


# Американская розетка
class UsaSocket:
    def __init__(self, fork):
        self.fork = fork

    def connect(self):
        self.fork.power_usa()


# Вставляем американскую вилку в американскую розетку.
uf = UsaFork()
us = UsaSocket(uf)
us.connect()
# >>> power on. Usa


class AdapterEuroInUsa:
    def __init__(self):
        self._euro_fork = EuroFork()

    def power_usa(self):
        self._euro_fork.power_euro()


# Вставляем евро-адаптер в американскую розетку.
ad = AdapterEuroInUsa()
us = UsaSocket(ad)
us.connect()
