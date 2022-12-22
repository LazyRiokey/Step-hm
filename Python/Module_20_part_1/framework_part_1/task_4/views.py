from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show_mult_table(request):
    mult_table = []
    for i in range(1, 11):
        for k in range(1, 11):
            mult_table.append(f"{i} * {k} = {i * k}")

    return render(request, "index.html", context={"table" : mult_table})