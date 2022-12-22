from django import forms

from .models import *


class HumanForms(forms.Form):

    first_name = forms.CharField(max_length=50, required=True, label="Имя", widget=forms.TextInput(attrs={"class": "input_first_name"}))
    last_name = forms.CharField(max_length=50,required=True, label="Фамилия", widget=forms.TextInput(attrs={"class": "input_last_name"}))
    age = forms.IntegerField(required=True, label="Возраст", widget=forms.NumberInput(attrs={"class": "input_age"}))
    gender = forms.CharField(required=True, label="Пол", widget=forms.Select(attrs={"class": "input_gender"}, choices=Human.GENDERS))
