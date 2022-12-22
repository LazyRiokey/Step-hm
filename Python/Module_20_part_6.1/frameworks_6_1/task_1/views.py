from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import WaterOrdersForm
from .models import WaterOrders

# Create your views here.


class OrderView(CreateView):

    form_class = WaterOrdersForm
    template_name = "task_1/add_order.html"
    success_url = reverse_lazy("OrdersListView")


class OrdersListView(ListView):

    model = WaterOrders
    template_name = "task_1/view_orders.html"
    context_object_name = "orders"
    
