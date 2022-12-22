from django.shortcuts import render, redirect

from .forms import HumanForms
from .models import Human
# Create your views here.


def add_human(request):
    if request.method == "POST":
        form = HumanForms(request.POST)
        if form.is_valid():
            human = Human.objects.create(**form.cleaned_data)
            return redirect("hello_human", human_id=human.pk)
    else:
        form = HumanForms()
    return render(request, "human/add_human.html", {"form": form})


def hello_human(request, human_id):
    human = Human.objects.get(pk=human_id)

    return render(request, "human/say_hello.html", {"human": human})