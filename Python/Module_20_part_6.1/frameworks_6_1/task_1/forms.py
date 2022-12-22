from django import forms

from .models import WaterOrders


class WaterOrdersForm(forms.ModelForm):
    class Meta:
        model = WaterOrders
        fields = [
            "last_name",
            "first_name",
            "e_mail",
            "contacts",
            "address",
            "months_of_delivery",
            "bottle_volume",
        ]
        widgets = {
            "last_name": forms.TextInput(attrs={"class": "last-name-input"}),
            "first_name": forms.TextInput(attrs={"class": "first-name-input"}),
            "e_mail": forms.TextInput(attrs={"class": "e-mail-input"}),
            "contacts": forms.TextInput(attrs={"class": "contacts-input"}),
            "address": forms.TextInput(attrs={"class": "address-input"}),
            "months_of_delivery": forms.Select(attrs={"class": "months-of-delivery-input"}),
            "bottle_volume": forms.Select(attrs={"class": "bottle-volume-input"})
        }