import socket
import json
import requests

# Заготовка кода взята отсюда:
# https://docs-python.ru/standart-library/modul-socket-setevoj-interfejs-python/

KEY = "e35d44cd1d792d4211171fa278bb0669"

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10000)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        # Принимаем данные порциями и ретранслируем их
        while True:
            city = connection.recv(20000)
            print(f'Получено: {city.decode()}')
            if city:
                print('Обработка данных...')
                city = city.title()
                res = requests.get(
                    "http://api.openweathermap.org/data/2.5/forecast",
                params={"q": city, "cnt": 40, "units": "metric", "lang": "ru", "APPID": KEY},
                )
                data = res.json()
                raw_data = json.dumps(data, ensure_ascii=False).encode("UTF-8")

                print('Отправка обратно клиенту.')

                connection.send(raw_data)

            else:
                print('Нет данных от:', client_address)
                break

    finally:
        # Очищаем соединение
        connection.close()