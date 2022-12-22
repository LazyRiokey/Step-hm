from django.contrib import admin

from .models import *

# Register your models here.


class PoetryAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "verse", "verse_theme"]
    list_display_links = ["id", "author"]


admin.site.register(Poetry, PoetryAdmin)


class VerseThemeAdmin(admin.ModelAdmin):
    list_display = ["id", "theme"]
    list_display_links = ["id", "theme"]


admin.site.register(VerseTheme)
