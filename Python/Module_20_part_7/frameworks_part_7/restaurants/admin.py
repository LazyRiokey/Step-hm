from django.contrib import admin
from .models import *

# Register your models here.


class RestrauntsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "specialization", "address", "site", "contacts"]


admin.site.register(Restaurants, RestrauntsAdmin)


class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


admin.site.register(Specializations, SpecializationsAdmin)
