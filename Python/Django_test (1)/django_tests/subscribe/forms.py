from django import forms


class SubscribeForms(forms.Form):
    GENDERS = [
        ("М", "Мужской"),
        ("Ж", "Женский"),
    ]

    first_name = forms.CharField(
        max_length=50,
        label="Имя",
        widget=forms.TextInput(attrs={"class": "input-subs-first-name"}),
    )
    last_name = forms.CharField(
        max_length=50,
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "input-subs-last-name"}),
    )
    age = forms.IntegerField(
        min_value=10,
        max_value=100,
        label="Возраст",
        widget=forms.NumberInput(attrs={"class": "input-subs-age"}),
    )
    gender = forms.CharField(
        label="Пол",
        widget=forms.Select(attrs={"class": "select-subs-gender"},choices=GENDERS),
    )
    e_mail = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(attrs={"class": "input-subs-email"})
    )
