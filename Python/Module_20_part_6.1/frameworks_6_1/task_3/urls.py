from django.urls import path

from .views import *

urlpatterns = [
    path("", GoodsListView.as_view(), name="GoodsListView"),
    path("search/", SearchGoods.as_view(), name="SearchGoods"),
]
