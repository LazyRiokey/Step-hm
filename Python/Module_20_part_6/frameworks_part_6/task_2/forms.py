from django import forms
from django.core.exceptions import ValidationError


from .models import Сritique


class СritiqueForm(forms.ModelForm):
    class Meta:
        model = Сritique
        fields = ["nickname", "rating", "review", "spoilers"]
        widgets = {
            "nickname": forms.TextInput(attrs={"class": "nickname-input"}),
            "rating": forms.NumberInput(attrs={"class": "rating-input"}),
            "review": forms.Textarea(attrs={"class": "review-input"}),
            "spoilers": forms.CheckboxInput(attrs={"class": "spoilers-input"}),
        }

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"]
        if len(nickname) < 3:
            raise ValidationError("Длина ника не может быть меньше 3-х символов!")
        return nickname

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating > 100 or rating < 1:
            raise ValidationError("Оценка должна быть от 1 до 100 !")
        return rating
