""" Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, произво-
дителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реа-
лизуйте доступ к отдельным полям через методы класса. """


print()
print('Task 1'.center(40, '*'))
print()


class Car:

    def __init__(self, model, year, manufacturer, eng_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.eng_capacity = eng_capacity
        self.color = color
        self.price = price
    
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
    
    def get_info(self):
        print(f'Марка автомобиля: {self.model}')
        print(f'Год выпуска: {self.year}')
        print(f'Производитель: {self.manufacturer}')
        print(f'Объём двигателя: {self.eng_capacity}')
        print(f'Цвет: {self.color}')
        print(f'Цена: {self.price}')

my_car_1 = Car('Модель', 'Год_выпуска', 'Производитель', 'Объём_двигателя', 'Цвет', 'Цена')
my_car_1.get_info()


""" Задание 2
Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса. """

print()
print('Task 2'.center(40, '*'))
print()


class Book:

    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    
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
    
    def get_info(self):
        print(f'Название книги: {self.title}')
        print(f'Год выпуска: {self.year}')
        print(f'Издатель: {self.publisher}')
        print(f'Жанр: {self.genre}')
        print(f'Автор: {self.author}')
        print(f'Цена: {self.price}')

my_book_1 = Book('Книга', 'Год_выпуска', 'Издатель', 'Жанр', 'Автор', 'Цена')
my_book_1.get_info()


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
        self.capacity = capacity
    
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
    
    def get_info(self):
        print(f'Название стадиона: {self.stad_name}')
        print(f'Дата открытия: {self.op_date}')
        print(f'Страна: {self.country}')
        print(f'Город: {self.city}')
        print(f'Вместимость: {self.capacity}')

my_stadium_1 = Stadium('Название_стадиона', 'Дата_открытия', 'Страна', 'Город', 'Вместимость')
my_stadium_1.get_info()