from django import forms
from django.core.exceptions import ValidationError
import re

from .models import *


class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = [
            "last_name",
            "first_name",
            "e_mail",
            "contacts",
            "product_name",
            "purchase_date",
            "problem_description",
        ]

        widgets = {
            "last_name": forms.TextInput(attrs={"class": "last-name-input"}),
            "first_name": forms.TextInput(attrs={"class": "first-name-input"}),
            "e_mail": forms.TextInput(attrs={"class": "e-mail-input"}),
            "contacts": forms.TextInput(attrs={"class": "contacts-input"}),
            "product_name": forms.TextInput(attrs={"class": "product-name-input"}),
            "purchase_date": forms.SelectDateWidget(
                attrs={"class": "purchase-date-input"}, years=range(2000, 2022 + 1)
            ),
            "problem_description": forms.Textarea(
                attrs={"class": "problem-description-area"}
            ),
        }

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not re.match(r"[а-яА-Я]+", last_name):
            raise ValidationError("Фамилия должна содержать только буквы!")
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not re.match(r"[а-яА-Я]+", first_name):
            raise ValidationError("Имя должно содержать только буквы!")
        return first_name

    def clean_e_mail(self):
        e_mail = self.cleaned_data["e_mail"]
        r_w = r"^(?=.{1,64}@)[A-Za-z0-9_-]+(\\.[A-Za-z0-9_-]+)*@[^-][A-Za-z0-9-]+(\\.[A-Za-z0-9-]+)*(\\.[A-Za-z]{2,})$"
        if not re.match(r_w, e_mail):
            raise ValidationError("Ваш адрес электронной почты некорректен!")
        return e_mail
