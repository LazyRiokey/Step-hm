"""framework_part_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from home_work.views import *


url_books_id_patters = [
    path("<int:book_id>/", check_book_id, name="check_book_id"),
    path("", best_books, name="best_books"),
]

url_writers_books_pattern = [
    path("", check_writers),
    path("<str:w_book>/", writers_books, name="writers_books"),
]


url_writers_patters = [
    path("<str:writer>/", include(url_writers_books_pattern)),
    path("", writers, name="writers"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_page, name="main_page"),
    path("writers/", include(url_writers_patters)),
    path("books/", include(url_books_id_patters)),
]
