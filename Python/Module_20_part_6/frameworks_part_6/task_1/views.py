from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import Review

# Create your views here.


def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            review = Review.objects.all()
            return render(request, "task_1/add_review.html", {"form": form, "review": review})
    else:
        form = ReviewForm()
    return render(request, "task_1/add_review.html", {"form": form})
