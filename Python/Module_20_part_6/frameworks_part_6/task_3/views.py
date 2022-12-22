from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator

from .models import People

# Create your views here.


class PeopleListView(ListView):
    model = People
    template_name = "task_3/people_list.html"
    

class FindPeople(PeopleListView):
    template_name = "task_3/find_people.html"
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["first_name"] = self.request.GET.get("first_name")
        context["last_name"] = self.request.GET.get("last_name")
        context["patronymic"] = self.request.GET.get("patronymic")
        context["city"] = self.request.GET.get("city")
        return context
    

    def get_queryset(self):
        return People.objects.filter(
            Q(last_name__exact=self.request.GET.get("last_name")) &
            Q(first_name__exact=self.request.GET.get("first_name")) &
            Q(patronymic__exact=self.request.GET.get("patronymic")) &
            Q(city__exact=self.request.GET.get("city")) 
        )
