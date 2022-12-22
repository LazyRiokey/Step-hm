import socket
import json

# Заготовка кода взята отсюда:
# https://docs-python.ru/standart-library/modul-socket-setevoj-interfejs-python/

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ("localhost", 10000)
print("Старт сервера на {} порт {}".format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

while True:
    # ждем соединения
    print("Ожидание соединения...")
    connection, client_address = sock.accept()
    try:
        print("Подключено к:", client_address)
        # Принимаем данные порциями и ретранслируем их
        while True:
            city = connection.recv(8192)
            city = city.decode()
            print(f"Получено: {city}")
            if city:
                print("Обработка данных...")
                weather = []

                with open("w_data.json", "r", encoding="UTF-8") as json_file:
                    raw_data = json.load(json_file)

                def get_weather(index: int, cur_data: str):
                    w_time = raw_data["list"][index]["dt_txt"][11:16]
                    w_city = raw_data["city"]["name"]
                    w_sky = raw_data["list"][index]["weather"][0]["description"].title()
                    w_temp = int(raw_data["list"][index]["main"]["temp"])
                    return {
                        "Дата": cur_data,
                        "Город": w_city,
                        "Время": w_time,
                        "Небо": w_sky,
                        "Температура": w_temp,
                        "Разделитель": "".center(30, "-"),
                    }

                print(
                    city,
                    type(city),
                    raw_data["city"]["name"],
                    type(raw_data["city"]["name"]),
                )

                if city == raw_data["city"]["name"]:
                    for index in range(0, 40):
                        cur_date = raw_data["list"][index]["dt_txt"]
                        if int(cur_date[11:13]) % 6 == 0:
                            if cur_date[11:13] == "06":
                                date = f"{cur_date[0:10]} - Утро".center(30, "-")
                                weather.append(get_weather(index, date))
                            elif cur_date[11:13] == "12":
                                date = f"{cur_date[0:10]} - День".center(30, "-")
                                weather.append(get_weather(index, date))
                            elif cur_date[11:13] == "18":
                                date = f"{cur_date[0:10]} - Вечер".center(30, "-")
                                weather.append(get_weather(index, date))
                            elif cur_date[11:13] == "00":
                                date = f"{cur_date[0:10]} - Ночь".center(30, "-")
                                weather.append(get_weather(index, date))
                else:
                    with open("error.json", "r", encoding="UTF-8") as json_file:
                        weather = json.load(json_file)

                raw_data = json.dumps(weather, ensure_ascii=False).encode("UTF-8")

                print("Отправка обратно клиенту.")

                connection.send(raw_data)

            else:
                print("Нет данных от:", client_address)
                break

    finally:
        # Очищаем соединение
        connection.close()
