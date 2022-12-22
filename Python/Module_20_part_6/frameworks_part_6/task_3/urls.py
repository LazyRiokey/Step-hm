from django.urls import path, include
import re

from .views import *

urlpatterns = [
    path("", PeopleListView.as_view(), name="find_people"),
    path("search/", FindPeople.as_view(), name="find_people"),
]
