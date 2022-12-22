from django.http import HttpResponse
from django.shortcuts import render

from datetime import date, datetime, timedelta

# Create your views here.

def program_day(request):
    result = date(datetime.now().year, 1, 1) + timedelta(days=255)
    return HttpResponse(f'In current year, the programmer\'s day is {result.strftime("%d/%m/%Y")}')