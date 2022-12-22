from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


# Create your views here.

def index(request):
    return HttpResponse(f'Current date = {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')