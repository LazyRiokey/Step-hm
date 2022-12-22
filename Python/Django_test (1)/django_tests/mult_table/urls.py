from django.urls import path

from .views import *

urlpatterns = [
    path("", get_mult_table, name="get_mult_table"),
]
