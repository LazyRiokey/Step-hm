from django.shortcuts import render

from django.views.generic import ListView, CreateView

from .models import Goods
from .forms import GoodsForm

# Create your views here.


class GoodsListView(ListView):
    model = Goods
    template_name = "task_3/view_goods.html"

    def get_queryset(self):
        return Goods.objects.filter(title__icontains=self.request.GET.get("title"))


class SearchGoods(CreateView):
    form_class = GoodsForm
    template_name = "task_3/search_goods.html"
