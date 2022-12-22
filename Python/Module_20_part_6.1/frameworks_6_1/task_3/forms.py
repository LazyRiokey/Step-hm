from django import forms

from .models import Goods


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ["title"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "title-input"})
        }