import json
import requests

# KEY = "e35d44cd1d792d4211171fa278bb0669"
# city = "Артёмовский"

# res = requests.get(
#     "http://api.openweathermap.org/data/2.5/forecast",
#     params={"q": city, "cnt": 40, "units": "metric", "lang": "ru", "APPID": KEY},
# )

# data = res.json()
# with open("w_data.json", "w", encoding="UTF-8") as file:
#     json.dump(data, file)
# # print(json.dumps(data, indent=4))

with open("w_data.json", "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)

weather = []

# def get_weather(index:int, cur_data:str):
#     w_time = data["list"][index]["dt_txt"][11:16]
#     w_city = data["city"]["name"]
#     w_sky = data["list"][index]["weather"][0]["description"].title()
#     w_temp = int(data["list"][index]["main"]["temp"])
#     return {
#         "Дата": cur_data,
#         "Город": w_city,
#         "Время": w_time,
#         "Небо": w_sky,
#         "Температура": w_temp,
#         "Разделитель": "".center(30,"-"),
#         }


# for index in range(0, 40):
#     cur_date = data["list"][index]["dt_txt"]
#     if int(cur_date[11:13]) % 6 == 0:
#         if cur_date[11:13] == "06":
#             date = f"{cur_date[0:10]} - Утро".center(30, "-")
#             weather.append(get_weather(index, date))
#         elif cur_date[11:13] == "12":
#             date = f"{cur_date[0:10]} - День".center(30, "-")
#             weather.append(get_weather(index, date))
#         elif cur_date[11:13] == "18":
#             date = f"{cur_date[0:10]} - Вечер".center(30, "-")
#             weather.append(get_weather(index, date))
#         elif cur_date[11:13] == "00":
#             date = f"{cur_date[0:10]} - Ночь".center(30, "-")
#             weather.append(get_weather(index, date))

def get_weather():
    # w_time = data["list"][index]["dt_txt"][11:16]
    # w_city = data["city"]["name"]
    # w_sky = data["list"][index]["weather"][0]["description"].title()
    # w_temp = int(data["list"][index]["main"]["temp"])
    return {
        "Город": "Не найден!",
        "Время": "Отсутствует!",
        "Небо": "Не найдено!",
        "Температура": "Не найдена",
        "Разделитель": "".center(30,"-"),
        }


# weather = get_weather(0)
# date = f"2022-09-09 - День".center(30, "-")
# w_dict = {
#     "Дата": date,
#     "Город": weather[0],
#     "Время": weather[1],
#     "Небо": weather[2],
#     "Температура": weather[3],
#     "Разделитель": "".center(30,"-"),
#     }

weather.append(get_weather())

with open("error.json", "w", encoding="UTF-8") as json_file:
    json.dump(weather, json_file)

with open("error.json", "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)

for i in data:
    for k, v in i.items():
        if k == "Дата" or k == "Разделитель":
            print(v)
        else:
            print(f"{k} : {v}")