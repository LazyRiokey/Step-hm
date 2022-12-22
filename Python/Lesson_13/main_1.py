""" Задание 1
К уже реализованному классу «Автомобиль» добавьте
конструктор, а также необходимые перегруженные методы.
"""


print()
print('Task 1'.center(40, '*'))
print()


class Car:

    def __init__(self, model, year, manufacturer, eng_capacity, color, price):
        self.model = model
        self.year = int(year)
        self.manufacturer = manufacturer
        self.eng_capacity = int(eng_capacity)
        self.color = color
        self.price = int(price)
    
    """ Перегруженные методы """

    def __lt__(self, other):
        if isinstance(other, Car):
            return f'''
            Год выпуска: {self.year < other.year}
            Объём двигателя: {self.eng_capacity < other.eng_capacity}
            Цена: {self.price < other.price}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __le__(self, other):
        if isinstance(other, Car):
            return f'''
            Год выпуска: {self.year <= other.year}
            Объём двигателя: {self.eng_capacity <= other.eng_capacity}
            Цена: {self.price <= other.price}'''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return f'''
            Марка автомобиля: {self.model == other.model}
            Год выпуска: {self.year == other.year}
            Производитель: {self.manufacturer == other.manufacturer}
            Объём двигателя: {self.eng_capacity == other.eng_capacity}
            Цвет: {self.color == other.color}
            Цена: {self.price == other.price}'''
        else:
            return 'Сравнивать можно только объекты класса!'

    def __ne__(self, other):
        if isinstance(other, Car):
            return f'''
            Марка автомобиля: {self.model != other.model}
            Год выпуска: {self.year != other.year}
            Производитель: {self.manufacturer != other.manufacturer}
            Объём двигателя: {self.eng_capacity != other.eng_capacity}
            Цвет: {self.color != other.color}
            Цена: {self.price != other.price}'''
        else:
            return 'Сравнивать можно только объекты класса!'
        
    def __gt__(self, other):
        if isinstance(other, Car):
            return f'''
            Год выпуска: {self.year > other.year}
            Объём двигателя: {self.eng_capacity > other.eng_capacity}
            Цена: {self.price > other.price}'''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __ge__(self, other):
        if isinstance(other, Car):
            return f'''
            Год выпуска: {self.year >= other.year}
            Объём двигателя: {self.eng_capacity >= other.eng_capacity}
            Цена: {self.price >= other.price}'''
        else:
            return 'Сравнивать можно только объекты класса!'

    """ Доступ к переменным класса """
    
    def set_model(self):
        self.model = input('Введите модель автомобиля: ')
    
    def set_year(self):
        self.year = input('Введите год выпуска автомобиля: ')
    
    def set_manufacturer(self):
        self.manufacturer = input('Введите производителя автомобиля: ')
    
    def set_eng_capacity(self):
        self.eng_capacity = input('Введите объём двигателя: ')
    
    def set_color(self):
        self.color = input('Введите цвет автомобиля: ')
    
    def set_price(self):
        self.price = input('Введите стоимость автомобиля: ')
    
    """ Вывод информации об объекте """
    
    def get_info(self):
        print(f'Марка автомобиля: {self.model}')
        print(f'Год выпуска: {self.year}')
        print(f'Производитель: {self.manufacturer}')
        print(f'Объём двигателя: {self.eng_capacity}')
        print(f'Цвет: {self.color}')
        print(f'Цена: {self.price}')

my_car_1 = Car('Модель', 2015, 'Производитель', 240, 'Цвет', 68000)
my_car_2 = Car('Модель_2', 2016, 'Производитель', 250, 'Цвет', 68000)

print(f'my_car_1 < my_car_2: {my_car_1 < my_car_2}')
print(f'my_car_1 <= my_car_2: {my_car_1 <= my_car_2}')
print(f'my_car_1 == my_car_2: {my_car_1 == my_car_2}')
print(f'my_car_1 != my_car_2: {my_car_1 != my_car_2}')
print(f'my_car_1 > my_car_2: {my_car_1 > my_car_2}')
print(f'my_car_1 >= my_car_2: {my_car_1 >= my_car_2}')

# my_car_1.get_info()


""" Задание 2
Задание 2
К уже реализованному классу «Книга» добавьте кон-
структор, а также необходимые перегруженные методы.
"""

print()
print('Task 2'.center(40, '*'))
print()


class Book:

    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = int(year)
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    
    """ Перегруженные методы """

    def __lt__(self, other):
        if isinstance(other, Book):
            return f'''
            Год выпуска: {self.year < other.year}
            Цена: {self.price < other.price}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __le__(self, other):
        if isinstance(other, Book):
            return f'''
            Год выпуска: {self.year <= other.year}
            Цена: {self.price <= other.price}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return f'''
            Название книги: {self.title == other.title}
            Год выпуска: {self.year == other.year}
            Издатель: {self.publisher == other.publisher}
            Жанр: {self.genre == other.genre}
            Автор: {self.author == other.author}
            Цена: {self.price == other.price}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'

    def __ne__(self, other):
        if isinstance(other, Book):
            return f'''
            Название книги: {self.title != other.title}
            Год выпуска: {self.year != other.year}
            Издатель: {self.publisher != other.publisher}
            Жанр: {self.genre != other.genre}
            Автор: {self.author != other.author}
            Цена: {self.price != other.price}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
        
    def __gt__(self, other):
        if isinstance(other, Book):
            return f'''
            Год выпуска: {self.year > other.year}
            Цена: {self.price > other.price}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __ge__(self, other):
        if isinstance(other, Book):
            return f'''
            Год выпуска: {self.year >= other.year}
            Цена: {self.price >= other.price}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    """ Доступ к переменным класса """
    
    def set_title(self):
        self.title = input('Введите название книги: ')
    
    def set_year(self):
        self.year = input('Введите год выпуска: ')
    
    def set_publisher(self):
        self.publisher = input('Введите издателя: ')
    
    def set_genre(self):
        self.genre = input('Введите жанр: ')
    
    def set_author(self):
        self.author = input('Введите автора: ')
    
    def set_price(self):
        self.price = input('Введите стоимость: ')

    """ Вывод информации об объекте """
    
    def get_info(self):
        print(f'Название книги: {self.title}')
        print(f'Год выпуска: {self.year}')
        print(f'Издатель: {self.publisher}')
        print(f'Жанр: {self.genre}')
        print(f'Автор: {self.author}')
        print(f'Цена: {self.price}')


my_book_1 = Book('Книга_1', 2020, 'Издатель_1', 'Жанр_1', 'Автор_1', 1440)
my_book_2 = Book('Книга_2', 2019, 'Издатель_1', 'Жанр_2', 'Автор_1', 1440)

print(f'my_book_1 < my_book_2: {my_book_1 < my_book_2}')
print(f'my_book_1 <= my_book_2: {my_book_1 <= my_book_2}')
print(f'my_book_1 == my_book_2: {my_book_1 == my_book_2}')
print(f'my_book_1 != my_book_2: {my_book_1 != my_book_2}')
print(f'my_book_1 > my_book_2: {my_book_1 > my_book_2}')
print(f'my_book_1 >= my_book_2: {my_book_1 >= my_book_2}')

# my_book_1.get_info()


""" Задание 3
Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса. """


print()
print('Task 3'.center(40, '*'))
print()


class Stadium:

    def __init__(self, stad_name, op_date, country, city, capacity):
        self.stad_name = stad_name
        self.op_date = op_date
        self.country = country
        self.city = city
        self.capacity = int(capacity)
    
    """ Перегруженные методы """

    def __lt__(self, other):
        if isinstance(other, Stadium):
            return f'''
            Вместимость: {self.capacity < other.capacity}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __le__(self, other):
        if isinstance(other, Stadium):
            return f'''
            Вместимость: {self.capacity <= other.capacity}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __eq__(self, other):
        if isinstance(other, Stadium):
            return f'''
            Название стадиона: {self.stad_name == other.stad_name}
            Дата открытия: {self.op_date == other.op_date}
            Страна: {self.country == other.country}
            Город: {self.city == other.city}
            Вместимость: {self.capacity == other.capacity}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'

    def __ne__(self, other):
        if isinstance(other, Stadium):
            return f'''
            Название стадиона: {self.stad_name != other.stad_name}
            Дата открытия: {self.op_date != other.op_date}
            Страна: {self.country != other.country}
            Город: {self.city != other.city}
            Вместимость: {self.capacity != other.capacity}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
        
    def __gt__(self, other):
        if isinstance(other, Stadium):
            return f'''
            Вместимость: {self.capacity > other.capacity}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    def __ge__(self, other):
        if isinstance(other, Stadium):
            return f'''
            Вместимость: {self.capacity >= other.capacity}
            '''
        else:
            return 'Сравнивать можно только объекты класса!'
    
    """ Доступ к переменным класса """

    def set_stad_name(self):
        self.stad_name = input('Введите название стадиона: ')
    
    def set_op_date(self):
        self.op_date = input('Введите дату открытия: ')
    
    def set_country(self):
        self.country = input('Введите страну: ')
    
    def set_city(self):
        self.city = input('Введите город: ')
    
    def set_capacity(self):
        self.capacity = input('Введите вместимость: ')
    
    """ Вывод информации об объекте """

    def get_info(self):
        print(f'Название стадиона: {self.stad_name}')
        print(f'Дата открытия: {self.op_date}')
        print(f'Страна: {self.country}')
        print(f'Город: {self.city}')
        print(f'Вместимость: {self.capacity}')

my_stadium_1 = Stadium('Название_стадиона', 'Дата_открытия', 'Страна', 'Город', 10000)
my_stadium_2 = Stadium('Название_стадиона_2', 'Дата_открытия_2', 'Страна', 'Город', 10000)

print(f'my_stadium_2 < my_stadium_2: {my_stadium_1 < my_stadium_2}')
print(f'my_stadium_2 <= my_stadium_2: {my_stadium_1 <= my_stadium_2}')
print(f'my_stadium_2 == my_stadium_2: {my_stadium_1 == my_stadium_2}')
print(f'my_stadium_2 != my_stadium_2: {my_stadium_1 != my_stadium_2}')
print(f'my_stadium_2 > my_stadium_2: {my_stadium_1 > my_stadium_2}')
print(f'my_stadium_2 >= my_stadium_2: {my_stadium_1 >= my_stadium_2}')

# my_stadium_1.get_info()