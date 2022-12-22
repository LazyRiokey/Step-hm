from django.contrib import admin

from .models import Goods, Category
# Register your models here.

class GoodsAdmin(admin.ModelAdmin):

    list_display = ["id", "title", "price", "quantity", "category"]


admin.site.register(Goods, GoodsAdmin)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ["id", "title"]

admin.site.register(Category, CategoryAdmin)
