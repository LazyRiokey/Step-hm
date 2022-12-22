from django.urls import path

from .views import *


urlpatterns = [
    path("", get_date, name="get_date"),
]
