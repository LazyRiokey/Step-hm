from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import ComplaintsForm
from .models import Complaints

# Create your views here.


class ComplaintsView(CreateView):

    form_class = ComplaintsForm
    template_name = "task_2/add_complaint.html"
    success_url = reverse_lazy("ComplaintsListView")


class ComplaintsListView(ListView):

    model = Complaints
    template_name = "task_2/view_complaints.html"
