from django.db import models
from django.urls import reverse

# Create your models here.


class WaterOrders(models.Model):
    MONTH_CHOICES = [
        ("1", "1 месяц"),
        ("3", "3 месяца"),
        ("6", "6 месяцев"),
        ("12", "12 месяцев"),
    ]

    BOTTLE_CHOICES = [("5", "5 литров"), ("10", "10 литров"), ("15", "15 литров")]

    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    e_mail = models.EmailField(verbose_name="E-mail")
    contacts = models.CharField(max_length=12, verbose_name="Контактный телефон")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    months_of_delivery = models.CharField(
        max_length=2, verbose_name=("Срок месяцев доставки"), choices=MONTH_CHOICES
    )
    bottle_volume = models.CharField(
        max_length=2, verbose_name="Объём баллона воды", choices=BOTTLE_CHOICES
    )
