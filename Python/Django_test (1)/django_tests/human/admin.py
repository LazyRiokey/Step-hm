from django.contrib import admin

from .models import *

# Register your models here.


class HumanAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "gender"]
    list_display_links = ["first_name", "last_name"]


admin.site.register(Human, HumanAdmin)
