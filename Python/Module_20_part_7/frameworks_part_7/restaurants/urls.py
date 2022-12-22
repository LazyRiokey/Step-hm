from django.urls import path
from .views import *

urlpatterns = [
    path("", RestaurantsView.as_view(), name="restraunts_info"),
    path("add_restraunt/", AddRestraunt.as_view(), name="add_restraunt"),
]