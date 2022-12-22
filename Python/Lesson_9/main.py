# import figures.circle.code as circle
# import figures.square.code as square
# import figures.triangle.code as triangle

# print("Circle")
# print(circle.circle_area())
# print(circle.circle_area(10))
# print(circle.circle_perimeter())
# print(circle.circle_perimeter(10))
# print()
# print("Square")
# print(square.square_area())
# print(square.square_area(5))
# print(square.square_perimeter())
# print(square.square_perimeter(5))
# print()
# print("Triangle")
# print(triangle.triangle_area())
# print(triangle.triangle_area(7, 8, 9))
# print(triangle.triangle_perimeter())
# print(triangle.triangle_perimeter(7, 8, 9))


# file = open('C:\\Users\\kuteg\\Desktop\\Step\\Python\\Lesson_9\\figures\\file1.txt', mode='w')

# for i in range(10):
#     s = 'line #' + str(i + 1) + '\n'
#     file.write(s)

# file.close()

# def read_lines(lines, file):
#     try:
#         if lines <= 0:
#             raise Exception
#         else:
#             my_file = open(file, 'r')
#             line = my_file.readlines()[-lines:]
#             for i in line:
#                 print(i)

#             my_file.close()
#     except Exception:
#         print("Something went wrong")

# read_lines(3, 'C:\\Users\\kuteg\\Desktop\\Step\\Python\\Lesson_9\\figures\\file.txt')

def longest_word(file):
    my_file = open(file, 'r', encoding='utf-8')
    word = my_file.read()
    word = word.split()
    max_lenght = len(max(word, key=len))
    words = [w for w in word if len(w) == max_lenght]
    return words

print(longest_word('C:\\Users\\kuteg\\Desktop\\Step\\Python\\Lesson_9\\figures\\file1.txt'))