from django.urls import path, include

from .views import *

urlpatterns = [
    path("", add_critique, name="add_critique"),
]