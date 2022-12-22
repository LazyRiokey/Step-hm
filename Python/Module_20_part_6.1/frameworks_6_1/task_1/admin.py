from django.contrib import admin

from .models import *

# Register your models here.


class WaterOrdersAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "last_name",
        "first_name",
        "e_mail",
        "contacts",
        "address",
        "months_of_delivery",
        "bottle_volume",
    ]
    list_display_links = ["id", "last_name"]


admin.site.register(WaterOrders, WaterOrdersAdmin)
