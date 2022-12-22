#!/usr/bin/env python3

__a, __b, __c = 7, 2, 8

def triangle_perimeter(a=__a, b=__b, c=__c):
    return a + b + c

def triangle_area(a=__a, b=__b, c=__c):
    p = triangle_perimeter(a, b, c)
    return (p * (p - a) - (p - b) - (p - c)) ** 0.5
