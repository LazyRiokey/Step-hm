# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
    
#     def __str__(self):
#         return self.name + ' in ' + self.galaxy

# sun = Star("Sun", "Milky Way")
# print(sun)


# import math


# class Area:

#     counter = 0

#     @staticmethod
#     def area_triangle_h_and_base(base, height):
#         Area.counter += 1
#         return 0.5 * base * height

#     @staticmethod
#     def area_triangle_two_side_and_angle(side1, side2, angle):
#         Area.counter += 1
#         return  0.5 * side1 * side2 * math.sin(angle)
    
#     @staticmethod
#     def area_square(side):
#         Area.counter += 1
#         return pow(side, 2)
    
#     @staticmethod
#     def area_rectangle(lenght, width):
#         Area.counter += 1
#         return lenght * width
    
#     @staticmethod
#     def area_rhombus(d1, d2):
#         Area.counter += 1
#         return (d1 * d2) / 2

#     @staticmethod
#     def count_static_method():
#         return Area.counter

# obj_1 = Area()
# print(obj_1.area_rectangle(5, 8))
# print(obj_1.area_square(5))
# print(Area.count_static_method())

import math


class Operations:

    @staticmethod
    def maximum(*args):
        return max(args)
    
    @staticmethod
    def minimum(*args):
        return min(args)
    
    @staticmethod
    def average(*args):
        result = 0
        for i in args:
            result += i
        
        return result / len(args)
    
    @staticmethod
    def factorial(arg):
        if arg == 0:
            return 1
        return factorial(arg - 1) * arg

obj = Operations()
print(obj.maximum(1, 2, 3, 4))
print(obj.minimum(1, 2, 3, 4))
print(obj.average(1, 2, 3, 4))
print(obj.factorial(10))