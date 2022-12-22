""" Задание 1
Написать рекурсивную функцию нахождения наи-
большего общего делителя двух целых чисел. """

def get_gcd(num_1, num_2):
    if num_2 == 0: 
        return num_1
    else:
        return get_gcd(num_2, num_1 % num_2)

result = get_gcd(16, 44)
print(result)

""" Задание 2
Написать игру «Быки и коровы». Программа «за-
гадывает» четырёхзначное число и играющий должен
угадать его. После ввода пользователем числа программа
сообщает, сколько цифр числа угадано (быки) и сколько
цифр угадано и стоит на нужном месте (коровы). После
отгадывания числа на экран необходимо вывести коли-
чество сделанных пользователем попыток. В программе
необходимо использовать рекурсию. """

from random import randint


def bulls_and_cows():
    number = ''
    counter = 0

    for _ in range(4):
        x = randint(0,9)
        number += str(x)
    
    
    while True:
        bulls = 0
        cows = 0
        counter += 1
        choice = input('Введите четырёхзначное число: ')

        for i in range(4):
            if number[i] == choice[i]:
                bulls += 1
            elif choice[i] in number:
                cows += 1
        print(f"{choice} содержит {str(bulls)} быка и {str(cows)} коровы")

        if bulls == 4:
            print(f"Загаданное число = {number}\nВы победили за {counter} хода(ов)")
            break

bulls_and_cows()


""" Задание 3
Дана шахматная доска размером 8×8 и шахматный конь.
Программа должна запросить у пользователя координаты
клетки поля и поставить туда коня. Задача программы
найти и вывести путь коня, при котором он обойдет все
клетки доски, становясь в каждую клетку только один
раз. (Так как процесс отыскания пути для разных началь-
ных клеток может затянуться, то рекомендуется сначала 
опробовать задачу на поле размером 6×6). В программе
необходимо использовать рекурсию. """


x_board, y_board = map(int, input("Введите размерность доски через пробел: ").split())
knight_position = input("Введите текующее положение коня (пример: A1, B3 и т.д.): ")
x0 = x_board - int(knight_position[1])
y0 = ord(knight_position[0]) - ord('A')
#Суммарное количество клеток доски.
cells_total = x_board * y_board
#Инициализация доски.
board = [[-1] * y_board for _ in range(x_board)]
visited = [[False] * y_board for _ in range(x_board)]
#Список допустимых ходов коня.
knight_moves = [(1, 2), (-1, -2),
                (2, 1), (-2, -1),
                (-1, 2), (1, -2),
                (-2, 1), (2, -1)]

#Функция проверки координат
#на соответствие границам доски.
def check_bounds(x, y):
    return -1 < x < x_board and -1 < y < y_board

#Функция проверки состояния клетки
#(посещена клетка или еще нет).
def is_visited(x, y):
    return visited[x][y]

#Функция, возвращающая список
#непосещённых клеток доски,
#на которые конь может пойти
#с данной позиции.
def get_move_list(x, y):
    available_moves = []
    for dx, dy in knight_moves:
        new_x, new_y = x + dx, y + dy
        if check_bounds(new_x, new_y):
            if not is_visited(new_x, new_y):
                available_moves.append((new_x, new_y))
    return available_moves

#Рекурсивная функция решения
#задачи о пути коня по доске.
#Возвращает True, если путь
#найден, и False иначе.
def tour(x, y, move_number):
    #Отмечаем текущую клетку
    #как посещенную.
    visited[x][y] = True
    #Если отмечаемый номер соответствует
    #суммарному количеству клеток доски,
    #то возвращаем True (нашли решение).
    answer = False
    if move_number == cells_total - 1:
        board[x][y] = move_number;
        answer = True
    else:
        move_list = get_move_list(x, y)
        if len(move_list) != 0:
            #Получение количества полей,
            #которые доступных с полей
            #из текущего списка.
            neighbors = [(len(get_move_list(xnew, ynew)), (xnew, ynew)) for xnew, ynew in move_list]
            #Определение минимального
            #количества полей, доступных
            #с клеток из списка.
            neighbors_min = min([pair[0] for pair in neighbors]) 
            #Отбор тех полей из списка,
            #с которых можно пойти на
            #минимальное число ещё не
            #пройденных полей.
            canditates = [pair[1] for pair in neighbors if pair[0] == neighbors_min]
            #Рекурсивно вызываем функцию
            #для каждого из полей-кандидатов,
            #пока не решим задачу или не
            #переберем всех кандидатов.
            for i, j in canditates:
                if tour(i, j, move_number + 1):
                    board[x][y] = move_number
                    answer = True
                    break
    visited[x][y] = False
    return answer

counter = 0

if tour(x0, y0, 0):
    for row in board:
        for elem in row:
            counter += 1
            if counter % len(row) == 0:
                counter = 0
                print(str(elem).center(4, " ") + "|", end="")
                print()
            else:
                print(str(elem).center(4, " ") + "|", end="")
else:
    print("Нет решения!")