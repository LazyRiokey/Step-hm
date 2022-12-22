from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("random_verse/", Oracle.as_view()),
    path("random_int/", RandomInt.as_view()),
    path("random_range_int/", RandomRangeInt.as_view()),
    path("random_list_int/", RandomListInt.as_view()),
]
