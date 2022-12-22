from django.contrib import admin

from .models import Сritique

# Register your models here.


class СritiqueAdmin(admin.ModelAdmin):
    list_display = ["id", "nickname", "rating", "review", "spoilers"]
    list_display_links = ["id", "nickname"]


admin.site.register(Сritique, СritiqueAdmin)
