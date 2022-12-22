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
        data = sock.recv(8192)
        amount_received += len(data)
        raw_data = json.loads(data.decode("UTF-8"))
        
        for i in raw_data:
            for k, v in i.items():
                if k == "Дата" or k == "Разделитель":
                    print(v)
                else:
                    print(f"{k} : {v}")

finally:
    print('Закрываем сокет')
    sock.close()