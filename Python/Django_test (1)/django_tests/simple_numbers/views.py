from django.shortcuts import render, HttpResponse
from sympy import isprime

from .forms import *
# Create your views here.

def get_simple(request):
    if request.method == "POST":
        form = SimpleNumbersForms(request.POST or None)
        if form.is_valid():
            start_range = form.cleaned_data.get("start_range")
            end_range = form.cleaned_data.get("end_range")
            prime_list = calculate(start_range, end_range)
            context = {
                "prime_list": prime_list,
                "start_range": start_range,
                "end_range": end_range,
            }
            return render(request, "simple_numbers/simple_table.html", context)
    else:
        form = SimpleNumbersForms()
    return render(request, "simple_numbers/simple.html", {"form": form})


def calculate(start, stop):
    prime_list = []
    for num in range(start, stop):
        if isprime(num) == True:
            prime_list.append(num)
    return prime_list