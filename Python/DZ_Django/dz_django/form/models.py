from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Contacts(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(
        validators=[phone_number_regex], max_length=16, unique=True
    )
    company = models.ForeignKey(
        "Company", verbose_name=("Компания"), on_delete=models.PROTECT
    )
    info = models.CharField(max_length=100, verbose_name="Информация")

    def __str__(self):
        return self.last_name

    class Meta:

        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class Company(models.Model):
    company = models.CharField(max_length=50, verbose_name="Компания")

    def __str__(self):
        return self.company

    class Meta:

        verbose_name = "Компания"
        verbose_name_plural = "Компании"
