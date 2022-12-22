from django.urls import path

from .views import *

urlpatterns = [
    path("add_order/", OrderView.as_view(), name="OrderView"),
    path("orders/", OrdersListView.as_view(), name="OrdersListView"),
]
