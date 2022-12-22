from django.shortcuts import render, redirect
from .forms import *
from .models import Contacts, Company

# Create your views here.


def all_contacts(request):
    contacts = Contacts.objects.all()

    return render(request, "form/contacts.html", {"contacts": contacts})


def add_new(request):
    if request.method == "POST":
        my_form = ContactsForms(request.POST)
        if my_form.is_valid():
            Contacts.objects.create(**my_form.cleaned_data)
            return redirect("all_contacts")
    else:
        my_form = ContactsForms()
    return render(request, "form/add_contact.html", {"form": my_form})
