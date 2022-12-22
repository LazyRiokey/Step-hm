# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = list(map(int, old_list))
# print(new_list)

# def is_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False

# x = is_triangle(6, 6, 15)
# print(x)

# import re

# def check_email(email):
#     regexp = r'^\w+@((\w+\.)+.)\w+'

#     if re.match(regexp, email):
#         print(True)
#     else:
#         print(False)

# check_email('admin@admin.com')

# def convert(my_list):
#     return list(set(my_list))

# my_list = [1, 1, 2, 2, 5, 8, 9, 4]
# new_list = convert(my_list)
# print(new_list)

# my_dict = {'Egor':'Kutaev'}

# def dict_unpacking(my_dict):
#     for k, v in my_dict.items():
#         print([f'key >> {k} - value >> {v}'])

# dict_unpacking(my_dict)

# def factorial(x):
#     if x == 1:
#         return x
#     else:
#         return x * factorial(x - 1)

# x = factorial(5)
# print(x)

