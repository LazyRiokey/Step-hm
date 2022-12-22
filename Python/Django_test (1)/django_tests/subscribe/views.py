from django.shortcuts import render

from .forms import *
# Create your views here.

def subscribtion(request):
    if request.method == "POST":
        form = SubscribeForms(request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            age = form.cleaned_data.get("age")
            gender = form.cleaned_data.get("gender")
            e_mail = form.cleaned_data.get("e_mail")
            context = {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "gender": gender,
                "e_mail": e_mail,
            }
            return render(request, "subscribe/show_sub.html", context)
    else:
        form = SubscribeForms()
    return render(request, "subscribe/sub.html", {"form": form})