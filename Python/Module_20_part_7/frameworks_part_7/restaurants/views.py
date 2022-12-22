from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views here.


class RestaurantsView(ListView):

    model = Restaurants
    template_name = "restaurants/all_info.html"


class AddRestraunt(FormView):

    form_class = RestrauntForm
    template_name = "restaurants/add_restraunt.html"
    template_name_field = "form"
    success_url = reverse_lazy("restraunts_info")

    def post(self, request, *args, **kwargs):
        form = RestrauntForm(request.POST)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
