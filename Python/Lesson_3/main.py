# while True:
#     try:
#         fib = int(input('Введите порядковый номер искомого числа Фибоначчи: '))
#     except Exception:
#         print("Произошла ошибка")
#     else:
#         x, y = 0, 1
#         for i in range(2, fib + 1):
#             x, y = y, x + y
#         print(y)