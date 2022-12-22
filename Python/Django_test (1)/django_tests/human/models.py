from django.db import models

# Create your models here.


class Human(models.Model):
    GENDERS = [
        ("М", "Мужской"),
        ("Ж", "Женский"),
    ]
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    gender = models.CharField(max_length=2, choices=GENDERS)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:

        verbose_name = "Человек"
        verbose_name_plural = "Люди"