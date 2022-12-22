""" Task 1 """


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


""" Task 2 """


class Square:

    def __init__(self, side):
        self.side = side

class Circle:

    def __init__(self, radius):
        self.radius = radius

class Calculate(Square, Circle):

    def __init__(self, side, radius):
        Square.__init__(self, side)
        Circle.__init__(self, radius)

    def r_through_the_side(self):
        if self.radius == self.side / 2:
            return True
        else:
            return False

obj = Calculate(7, 14)
print(obj.r_through_the_side())
    

""" Task 3 """


class Wheels:

    def __init__(self, wheels):
        self.wheels = wheels


class Engine:

    def __init__(self, engine):
        self.engine = engine


class Doors:

    def __init__(self, doors):
        self.doors = doors


class Car(Wheels, Engine, Doors):

    def __init__(self, car, wheels, engine, doors):
        Wheels.__init__(self, wheels)
        Engine.__init__(self, engine)
        Doors.__init__(self, doors)
        self.car = car
    
    def get_car(self):
        print(f'Car >> {self.car}\nEngine >> {self.engine}\nWheels >> {self.wheels}\nDoors >> {self.doors}')

car_obj = Car('Car_name', 'Wheels', 'Engine', 'Doors')
car_obj.get_car()


""" Task 4 """


class Employeer:

    def print(self):
        print(f'This is {__class__.__name__} class!')


class President(Employeer):

    def print(self):
        print(f'This is {__class__.__name__} class!')


class Manager(Employeer):

    def print(self):
        print(f'This is {__class__.__name__} class!')


class Worker(Employeer):

    def print(self):
        print(f'This is {__class__.__name__} class!')


empl_obj = Employeer()
empl_obj.print()

pres_obj = President()
pres_obj.print()

manager_obj = Manager()
manager_obj.print()

worker_obj = Worker()
worker_obj.print()


""" Task 5 """


class Employeer:

    def __init__(self, age):
        self.age = age
    
    def __str__(self):
        return f'Class {self.__class__.__name__} >> Age {self.age}'


class President(Employeer):

    def print(self):
        print('This is President class!')


class Manager(Employeer):

    def print(self):
        print('This is Manager class!')


class Worker(Employeer):

    def print(self):
        print('This is Worker class!')


empl_obj = Employeer(22)
print(empl_obj)
pres_obj = President(24)
print(pres_obj)
manager_obj = Manager(25)
print(manager_obj)
worker_obj = Worker(26)
print(worker_obj)
