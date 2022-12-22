import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["nickname", "stars", "mail", "review"]
        widgets = {
            "nickname": forms.TextInput(attrs={"class": "nickname-input"}),
            "stars": forms.NumberInput(attrs={"class": "stars-input"}),
            "mail": forms.EmailInput(attrs={"class": "email-input"}),
            "review": forms.Textarea(attrs={"class": "review-input"}),
        }
    
    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"]
        if len(nickname) < 3:
            raise ValidationError("Длина ника не может быть меньше 3-х символов!")
        return nickname
    
    def clean_stars(self):
        stars = self.cleaned_data["stars"]
        if stars > 5 or stars < 1:
            raise ValidationError("Оценка должна быть от 1 до 5 звёзд!")
        return stars

    def clean_mail(self):
        mail = self.cleaned_data["mail"]
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail):
            raise ValidationError("Введёный адрес не верный!")
        return mail

