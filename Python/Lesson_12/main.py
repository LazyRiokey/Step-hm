# class Sample:

#     def __init__(self, name):
#         print('Я появился!')
#         self.name = name
    
#     def getName(self):
#         print(self.name)

# my_obj = Sample('Any_name')
# my_obj.getName()


# class Human:

#     def __init__(self, name=None, surname=None, patronymic=None, birthday=None, city=None, country=None, adress=None):
#         self.name = name
#         self.surname = surname
#         self.patronymic = patronymic
#         self.birthday = birthday
#         self.city = city
#         self.country = country
#         self.adress = adress
    
#     def set_name(self):
#         self.name = input('Name: ')
    
#     def set_surname(self):
#         self.surname = input('Surname: ')
    
#     def set_patronymic(self):
#         self.patronymic = input('Patronymic: ')
    
#     def set_birthday(self):
#         self.birthday = input('Birthday: ')
    
#     def set_city(self):
#         self.city = input('City: ')
    
#     def set_country(self):
#         self.country = input('Country: ')
    
#     def set_addres(self):
#         self.adress = input('Adress: ')
    
#     def getHuman(self):
#         print(f"""
#         Full name = {self.name} {self.surname} {self.patronymic}
#         Birthday = {self.birthday}
#         City = {self.city}
#         Country = {self.country}
#         Adress = {self.adress}
#         """)

# obj = Human('Иванов', 'Иван', 'Иванович', '01.01.1990', 'Город', 'Страна', 'Адрес')
# obj.getHuman()
# obj_2 = Human()
# obj_2.getHuman()

# class City:

#     def __init__(self, city_name=None, region=None, country=None, inhabitants=None, postcode=None, tel_area_code=None):
#         self.city_name = city_name
#         self.region = region
#         self.country = country
#         self.inhabitants = inhabitants
#         self.postcode = postcode
#         self.tel_area_code = tel_area_code
    
#     def set_city(self):
#         self.city_name = input('City name: ')
    
#     def set_region(self):
#         self.region = input('Region name: ')
    
#     def set_country(self):
#         self.country = input('Country name: ')
    
#     def set_inhabitants(self):
#         self.inhabitants = input('Inhabitants: ')
    
#     def set_postcode(self):
#         self.postcode = input('Postcode: ')
    
#     def set_tel_area_code(self):
#         self.tel_area_code = input('Telephone area code: ')
    
#     def get_info(self):
#         print(f"""
#         City: {self.city_name}
#         Region: {self.region}
#         Country: {self.country}
#         Inhabitants: {self.inhabitants}
#         Postcode: {self.postcode}
#         Telephone area code: {self.tel_area_code}
#         """)

# my_obj_1 = City('City', 'Region', 'Country', '123456', '654321', '6549841')
# my_obj_1.get_info()
# my_obj_2 = City()
# my_obj_2.set_city()
# my_obj_2.get_info()


# class Country:

#     def __init__(self, country=None, continent=None, inhabitants=None, tel_area_code=None, capital=None, *cities):
#         self.country = country
#         self.continent = continent
#         self.inhabitants = inhabitants
#         self.tel_area_code = tel_area_code
#         self.capital = capital
#         self.cities = cities
    
#     def set_country(self):
#         self.country = input('Country name: ')

#     def set_continent(self):
#         self.continent = input('Continent name: ')
    
#     def set_inhabitants(self):
#         self.inhabitants = input('Inhabitants: ')

#     def set_tel_area_code(self):
#         self.tel_area_code = input('Telephone area code: ')

#     def set_capital(self):
#         self.capital = input('Capital name: ')
      
#     def set_cities(self):
#         self.cities = input('Cities: ')
    
#     def get_info(self):
#         print(f"""
#         Country: {self.country}
#         Continent: {self.continent}
#         Inhabitants: {self.inhabitants}
#         Telephone area code: {self.tel_area_code}
#         Capital: {self.capital}
#         Cities: {self.cities}
#         """)

# new_obj_4 = Country()
# new_obj_4.get_info()

# new_obj_5 = Country('Country', 'Continent', '654896', '32213', 'Capital', 'City_1', 'City_2', 'City_3', 'City_4')
# new_obj_5.get_info()


class Fraction:

    def __init__(self, nom_1=None, denom_1=None, nom_2=None, denom_2=None):
        self.nom_1 = nom_1
        self.denom_1 = denom_1
        self.nom_2 = nom_2
        self.denom_2 = denom_2
        self.result = None
    
    def set_first_div(self):
        self.nom_1 = int(input('Введите числитель: '))
        self.denom_1 = int(input('Введите знаменатель: '))
    
    def set_second_div(self):
        self.nom_2 = int(input('Введите числитель: '))
        self.denom_2 = int(input('Введите знаменатель: '))
    
    def get_sum(self):
        if self.denom_1 == self.denom_2:
            self.result = (self.nom_1 + self.nom_2) / self.denom_1
        else:
            self.result = (((self.nom_1 * self.denom_2) + (self.nom_2 * self.denom_1)) / (self.denom_1 * self.denom_2))
        self.get_result()
    
    def get_sub(self):
        if self.denom_1 == self.denom_2:
            self.result = (self.nom_1 - self.nom_2) / self.denom_1
        else:
            self.result = (((self.nom_1 * self.denom_2) - (self.nom_2 * self.denom_1)) / (self.denom_1 * self.denom_2))
        self.get_result()
    
    def get_mult(self):
        self.result = (self.nom_1 * self.nom_2) / (self.denom_1 * self.denom_2)
        self.get_result()
    
    def get_div(self):
        self.result = (self.nom_1 * self.denom_2) / (self.denom_1 * self.nom_2)
        self.get_result()
    
    def get_result(self):
        print(self.result)

obj = Fraction()
obj.set_first_div()
obj.set_second_div()
obj.get_sum()
print(obj.nom_1)
