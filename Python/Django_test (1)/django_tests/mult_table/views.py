from django.shortcuts import render
from sympy import isprime

from .forms import *
# Create your views here.

def get_mult_table(request):
    if request.method == "POST":
        form = MultTablesForms(request.POST or None)
        if form.is_valid():
            start_range = form.cleaned_data.get("start_range")
            end_range = form.cleaned_data.get("end_range")
            mult_table = calculate(start_range, end_range)
            context = {
                "mult_table": mult_table,
                "start_range": start_range,
                "end_range": end_range,
            }
            return render(request, "mult_table/show_mult_table.html", context)
    else:
        form = MultTablesForms()
    return render(request, "mult_table/mult_table.html", {"form": form})


def calculate(start, stop):
    mult_table = []

    for i in range(start, stop + 1):
        for k in range(1, 11):
            mult_table.append(f"{i} * {k} = {i * k}")
    return mult_table