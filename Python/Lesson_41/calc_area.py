from math import pi


def calc_area(radius):
    if type(radius) not in (int, float):
        raise TypeError("Radius must be a number!")
    elif radius < 0:
        raise ValueError("Radius must be > 0")
    return pi * pow(radius, 2)


# print(calc_area("Hello"))
