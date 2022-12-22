from django import forms
from django.core.exceptions import ValidationError
import re

from .models import Restaurants


class RestrauntForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ["title", "specialization", "address", "site", "contacts"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "input-title"}),
            "specialization": forms.Select(attrs={"class": "input-specialization"}),
            "address": forms.TextInput(attrs={"class": "input-address"}),
            "site": forms.TextInput(attrs={"class": "input-site"}),
            "contacts": forms.TextInput(attrs={"class": "input-contacts"}),
        }

    def clean_contacts(self):
        contacts = self.cleaned_data["contacts"]

        if not re.match(
            r'^\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})',
            contacts,
        ):
            raise ValidationError("Вы ввели некорректный номер телефона!")
        return contacts


