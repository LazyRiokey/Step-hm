import json
import socket
import sys

# Заготовка кода взята отсюда:
# https://docs-python.ru/standart-library/modul-socket-setevoj-interfejs-python/

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

try:
    # Отправка данных
    city = input("Введите название города на RU: ")
    print(f'Отправка: {city}')
    message = city.encode()
    sock.sendall(message)
    
    # Смотрим ответ
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(20000)
        amount_received += len(data)
        raw_data = json.loads(data.decode("UTF-8"))

        def get_weather(index):
            w_time = raw_data["list"][index]["dt_txt"][11:16]
            w_city = raw_data["city"]["name"]
            w_sky = raw_data["list"][index]["weather"][0]["description"].title()
            w_temp = int(raw_data["list"][index]["main"]["temp"])
            print(f"Город: {w_city}\nВремя: {w_time}\nНебо: {w_sky}\nТемпература: {w_temp}°")

        for index in range(0, 40):
            time = raw_data["list"][index]["dt_txt"]
            if time[11:13] == "06":
                print(f"{time[0:10]} - Утро".center(30, "-"))
                get_weather(index)
                print("".center(30,"-"))
            elif time[11:13] == "12":
                print(f"{time[0:10]} - День".center(30, "-"))
                get_weather(index)
                print("".center(30,"-"))
            elif time[11:13] == "18":
                print(f"{time[0:10]} - Вечер".center(30, "-"))
                get_weather(index)
                print("".center(30,"-"))
            elif time[11:13] == "00":
                print(f"{time[0:10]} - Ночь".center(30, "-"))
                get_weather(index)
                print("".center(30,"-"))

finally:
    print('Закрываем сокет')
    sock.close()