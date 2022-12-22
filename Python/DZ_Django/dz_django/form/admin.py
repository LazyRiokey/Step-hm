from django.contrib import admin
from .models import Contacts, Company

# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "phone_number", "company", "info"]


admin.site.register(Contacts, ContactsAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "company"]


admin.site.register(Company, CompanyAdmin)
