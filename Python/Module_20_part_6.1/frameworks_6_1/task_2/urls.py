from django.urls import path

from .views import *

urlpatterns = [
    path("add_complaint/", ComplaintsView.as_view(), name="ComplaintsView"),
    path("complaints/", ComplaintsListView.as_view(), name="ComplaintsListView"),
]
