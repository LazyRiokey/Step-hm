from django import forms


class MultTablesForms(forms.Form):

    start_range = forms.IntegerField(
        min_value=0,
        label="Начало диапазона",
        widget=forms.NumberInput(attrs={"class": "input-start-range"}),
    )
    end_range = forms.IntegerField(
        min_value=0,
        label="Конец диапазона",
        widget=forms.NumberInput(attrs={"class": "input-end-range"}),
    )
