from django.contrib import admin

from .models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id" ,"nickname", "stars", "mail", "review"]
    list_display_links = ["id", "nickname"]

admin.site.register(Review, ReviewAdmin)
