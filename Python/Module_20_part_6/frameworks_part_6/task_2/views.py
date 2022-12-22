from django.shortcuts import render

from .models import Сritique
from .forms import СritiqueForm

# Create your views here.


def add_critique(request):
    if request.method == "POST":
        form = СritiqueForm(request.POST)
        if form.is_valid():
            form.save()
            review = Сritique.objects.all()
            return render(
                request, "task_2/add_critique.html", {"form": form, "review": review}
            )
    else:
        form = СritiqueForm()
    return render(request, "task_2/add_critique.html", {"form": form})
