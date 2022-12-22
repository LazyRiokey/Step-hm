from django.contrib import admin

from .models import *

# Register your models here.


class ComplaintsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "last_name",
        "first_name",
        "e_mail",
        "contacts",
        "product_name",
        "purchase_date",
        "problem_description",
    ]
    list_display_links = ["id", "last_name"]


admin.site.register(Complaints, ComplaintsAdmin)
