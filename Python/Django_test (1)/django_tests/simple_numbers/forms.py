from django import forms


class SimpleNumbersForms(forms.Form):

    start_range = forms.IntegerField(min_value=0, label="Начало диапазона", widget=forms.NumberInput(attrs={"class": "input_start_range"}))
    end_range = forms.IntegerField(min_value=0, label="Конец диапазона", widget=forms.NumberInput(attrs={"class": "input_end_range"}))


