#!/usr/bin/env python3

import math

__default_radius = 5

def circle_perimeter(radius=__default_radius):
    return 2 * math.pi * radius

def circle_area(radius=__default_radius):
    return math.pi * pow(radius, 2)
