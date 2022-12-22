from django.contrib import admin
from django.urls import path

from first_app.views import *


urlpatterns = [
    path("", hello_world, name="index"),
    path("<str:country>", country_world, name="country_world"),
]
