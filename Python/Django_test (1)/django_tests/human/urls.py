from django.urls import path, include

from .views import *

urlpatterns = [
    path("", add_human, name="add_human"),
    path("<int:human_id>/", hello_human, name="hello_human"),
]
