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

def get_weather(index):
    w_time = data["list"][index]["dt_txt"][11:16]
    w_city = data["city"]["name"]
    w_sky = data["list"][index]["weather"][0]["description"].title()
    w_temp = int(data["list"][index]["main"]["temp"])
    print(f"Город: {w_city}\nВремя: {w_time}\nНебо: {w_sky}\nТемпература: {w_temp}°")

for index in range(0, 40):
    time = data["list"][index]["dt_txt"]
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
