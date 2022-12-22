""" Task 1 """


class Human:

    def __init__(self, birth, surname, name, patr, city):
        self.birth = birth
        self.surname = surname
        self.name = name
        self.patr = patr
        self.city = city
    
    def set_birth(self):
        self.birth = input('Введите дату рождения: ')
    
    def set_surname(self):
        self.surname = input('Введите фамилию: ')
    
    def set_name(self):
        self.name = input('Введите имя: ')
    
    def set_patr(self):
        self.patr = input('Введие отчество: ')
    
    def set_city(self):
        self.city = input('Введите город: ')
    
    def get_info(self):
        print(f"""
        ФИО = {self.surname} {self.name} {self.patr}
        Дата рождения: {self.birth}
        Город: {self.city}
        """)

class Builder(Human):

    def __init__(self, birth, surname, name, patr, city, company=None, pos=None):
        super().__init__(birth, surname, name, patr, city)
        self.company = company
        self.pos = pos
    
    def set_company(self):
        self.company = input('Введите название компании: ')
    
    def set_pos(self):
        self.pos = input('Введите занимаемую должность: ')
    
    def get_info(self):
        super().get_info()
        print(f"""
        Место работы: {self.company}
        Занимаемая должность: {self.pos}
        """)

class Sailor(Human):

    def __init__(self, birth, surname, name, patr, city, company=None, sea=None):
        super().__init__(birth, surname, name, patr, city)
        self.company = company
        self.sea = sea
    
    def set_company(self):
        self.company = input('Введите название компании: ')
    
    def set_sea(self):
        self.pos = input('Введите название моря: ')
    
    def get_info(self):
        super().get_info()
        print(f"""
        Место работы: {self.company}
        Море: {self.sea}
        """)

class Pilot(Human):

    def __init__(self, birth, surname, name, patr, city, company=None, plane=None):
        super().__init__(birth, surname, name, patr, city)
        self.company = company
        self.plane = plane
    
    def set_company(self):
        self.company = input('Введите название компании: ')
    
    def set_plane(self):
        self.plane = input('Введите название самолёта: ')
    
    def get_info(self):
        super().get_info()
        print(f"""
        Место работы: {self.company}
        Самолёт: {self.plane}""")
    

obj_1 = Human('01.01.1990', 'Иванов', 'Иван', 'Иванович', 'Название_города')
obj_2 = Builder('01.01.1990', 'Иванов', 'Иван', 'Иванович', 'Название_города', 'Название_компании', 'Занимаемая_должность')
obj_3 = Sailor('01.01.1990', 'Иванов', 'Иван', 'Иванович', 'Название_города', 'Название_компании', 'Название_моря')
obj_4 = Pilot('01.01.1990', 'Иванов', 'Иван', 'Иванович', 'Название_города', 'Название_компании', 'Название_самолёта')
obj_4.get_info()


""" Task 2 """


class Passport:

    def __init__(self, surname, name, patr, birth, place_of_birth, serial, num, date_of_issued):
        self.surname = surname
        self.name = name
        self.patr = patr
        self.birth = birth
        self.place_of_birth = place_of_birth
        self.serial = serial
        self.num = num
        self.date_of_issued = date_of_issued
    
    def set_surname(self):
        self.surname = input('Введите фамилию: ')

    def set_name(self):
        self.name = input('Введите имя: ')

    def set_patr(self):
        self.patr = input('Введие отчество: ')

    def set_birth(self):
        self.birth = input('Введите дату рождения: ')
    
    def set_place_of_birth(self):
        self.place_of_birth = input('Введите место рождения: ')
    
    def set_serial(self):
        self.serial = input('Введите серию пасспорта: ')
    
    def set_num(self):
        self.num = input('Введите номер пасспорта: ')
    
    def set_date_of_issued(self):
        self.date_of_issued = input('Введите номер пасспорта: ')
    
    def get_info(self):
        print(f"""
        ФИО: {self.surname} {self.name} {self.patr}
        Дата рождения: {self.birth}
        Место рождения: {self.place_of_birth}
        Серия пасспорта: {self.serial}
        Номер пасспорта: {self.num}
        """)

class ForeignPassport(Passport):

    def __init__(self, surname, name, patr, birth, place_of_birth, serial, num, date_of_issued, visa_inf, foreign_num):
        super().__init__(surname, name, patr, birth, place_of_birth, serial, num, date_of_issued)
        self.visa_inf = visa_inf
        self.foreign_num = foreign_num
    
    def set_visa_info(self):
        self.visa_inf = input('Введите информацию о ранее выданных визах: ')
    
    def set_foreign_num(self):
        self.foreign_num = input('Введите номер загранпасспорта: ')
    
    def get_info(self):
        super().get_info()
        print(f"""
        Информация о ранее выданных визах: {self.visa_inf}
        Номер загранпасспорта: {self.foreign_num}
        """)

obj_5 = Passport('Иванов', 'Иван', 'Иванович', '01.01.1990', 'Место рождения', '1234', '123456', '02.02.2016')
obj_5.get_info()
obj_6 = ForeignPassport('Иванов', 'Иван', 'Иванович', '01.01.1990', 'Место рождения', '1234', '123456', '02.02.2016', 'Информация...', '12 1234567')
obj_6.get_info()


""" Task 3 """


class Animal:

    def __init__(self, name, type, place, color, subspec):
        self.name = name
        self.type = type
        self.place = place
        self.color = color
        self.subspec = subspec
    
    def get_info(self):
        print(f"""
        Название животного: {self.name}
        Тип животного: {self.type}
        Место обитания: {self.place}
        Окрас: {self.color}
        Подвид: {self.subspec}
        """)

class Tiger(Animal):

    def __init__(self, name='Тигры', type='Плотоядный', place='Индия', color='Ржаво-коричневый', subspec='Кошачьи' ):
        super().__init__(name, type, place, color, subspec)

obj_7 = Tiger()
obj_7.get_info()


""" Task 4 """


class Number:

    def __init__(self, number):
        self.number = number
    
    def __add__(self, other):
        return self.number + other.number
    
    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number
    
    def __truediv__(self, other):
        return self.number / other.number
    
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.number == other.number
        elif isinstance(other, int):
            return self.number == other
    
    def __ne__(self, other):
        if isinstance(other, Number):
            return self.number != other.number
        elif isinstance(other, int):
            return self.number != other
    
    def __it__(self, other):
        if isinstance(other, Number):
            return self.number < other.number
        elif isinstance(other, int):
            return self.number < other
    
    def __gt__(self, other):
        if isinstance(other, Number):
            return self.number > other.number
        elif isinstance(other, int):
            return self.number > other
    
    def __le__(self, other):
        if isinstance(other, Number):
            return self.number <= other.number
        elif isinstance(other, int):
            return self.number <= other
    
    def __ge__(self, other):
        if isinstance(other, Number):
            return self.number >= other.number
        elif isinstance(other, int):
            return self.number >= other
    
    
num_1 = Number(10)
num_2 = Number(20)
print(num_1 >= num_2)
print(f'{num_1.number} + {num_2.number} = {num_1 + num_2}')
print(f'{num_1.number} - {num_2.number} = {num_1 - num_2}')
print(f'{num_1.number} * {num_2.number} = {num_1 * num_2}')
print(f'{num_1.number} / {num_2.number} = {num_1 / num_2}')