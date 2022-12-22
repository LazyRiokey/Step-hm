import random
from datetime import datetime, timedelta


def gen_datetime(min_year, max_year):
    start = datetime(min_year, 1, 1, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


# with open("Lesson_24\modules\sql_gen.txt", "a+", encoding="utf-8") as data:
#   for _ in range(50):
#     dt_1 = (gen_datetime(2015, 2022))
#     dt_2 = dt_1 + timedelta(minutes=random.randint(0, 60), hours=random.randint(2, 18))
#     my_str_1 = (random.randint(1, 16), 1, str(dt_1)[:16], str(dt_2)[:16], random.randint(30, 60), random.randint(10, 20))
#     my_str_2 = (random.randint(1, 16), 2, str(dt_1)[:16], str(dt_2)[:16], random.randint(90, 120), random.randint(10, 32))
#     my_str_3 = (random.randint(1, 16), 3, str(dt_1)[:16], str(dt_2)[:16], random.randint(90, 140), random.randint(20, 56))
#     my_str_4 = (random.randint(1, 16), 4, str(dt_1)[:16], str(dt_2)[:16], random.randint(200, 300), random.randint(20, 60))
#     data.write(str(my_str_1) + "," + "\n")
#     data.write(str(my_str_2) + "," + "\n")
#     data.write(str(my_str_3) + "," + "\n")
#     data.write(str(my_str_4) + "," + "\n")

with open("Lesson_24\modules\male_names_rus.txt", "r", encoding="utf-8") as data:
  names = data.readlines()

with open("Lesson_24\modules\male_surnames_rus.txt", "r", encoding="utf-8") as data:
  surnames = data.readlines()


with open("Lesson_24\modules\sql_gen.txt", "a+", encoding="utf-8") as data:
  for _ in range(100):
    flight = random.randint(1008, 2007)
    fl_class = random.choice(["Economy", "Business"])
    price = random.randint(4000, 80000)
    first_name = random.choice(names).replace("\n","")
    last_name = random.choice(surnames).replace("\n","")
    ticket = (flight, fl_class, price, first_name, last_name)
    data.write(str(ticket) + "," + "\n")