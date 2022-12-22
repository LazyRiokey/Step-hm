from django.contrib import admin

from .models import People

# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "first_name", "patronymic", "city"]
    list_display_links = ["id", "last_name"]


admin.site.register(People, PeopleAdmin)
