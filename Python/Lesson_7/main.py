# def to_dict(lst):
#     result_dict = {x: x for x in lst}
#     print(result_dict)

# my_lst = [1, 2, 3, 4, 5, 6]
# to_dict(my_lst)

# def bread(function):
#     def wrapper():
#         function()
#         print("\______/")
#     return wrapper

# def ingredients(function):
#     def wrapper():
#         print(" Tomatoes")
#         function()
#         print(" Salad")
#     return wrapper

# @bread
# @ingredients
# def sandwich():
#     print(" Bacon")

# sandwich()