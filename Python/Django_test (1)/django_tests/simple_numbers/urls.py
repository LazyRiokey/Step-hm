from django.urls import path, include

from .views import *

urlpatterns = [
    path("", get_simple, name="get_simple"),
]
