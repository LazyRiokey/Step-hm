from django import forms
from .models import Company


class ContactsForms(forms.Form):

    first_name = forms.CharField(
        max_length=50,
        label="Имя",
        widget=forms.TextInput(attrs={"class": "first_name_input", "placeholder": "Введите имя.."}),
    )
    last_name = forms.CharField(
        max_length=50,
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "last_name_input", "placeholder": "Введите фамилию.."}),
    )
    phone_number = forms.CharField(
        max_length=16,
        label="Номер телефона",
        widget=forms.TextInput(attrs={"class": "phone_number_input", "placeholder": "+71234567890"}),
    )
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        label="Компания",
        empty_label="Выбор компании",
        required=True,
    )
    info = forms.CharField(
        max_length=100,
        label="Информация",
        widget=forms.Textarea(attrs={"class": "info_input", "placeholder": "Введите информацию о контакте.."}),
    )
