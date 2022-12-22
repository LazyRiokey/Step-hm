from django.shortcuts import render
from datetime import datetime

# Create your views here.

def get_date(request):
    cur_date = int(str(datetime.time(datetime.now()))[0:2])
    print(cur_date)
    if cur_date >= 6 and cur_date < 12:
        my_string = "Доброе утро!"
    elif cur_date >= 12 and cur_date < 18: 
        my_string = "Добрый день!"
    elif cur_date >= 18 and cur_date < 24:
        my_string = "Добрый вечер!"
    else:
        my_string = "Доброй ночи!"
    return render(request, "date_display/cur_date.html", {"my_string": my_string})