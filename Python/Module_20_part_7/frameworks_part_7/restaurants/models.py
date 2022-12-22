from django.db import models

# Create your models here.


class Restaurants(models.Model):

    title = models.CharField(max_length=100, verbose_name="Название")
    specialization = models.ForeignKey(
        "Specializations", on_delete=models.PROTECT, null=True
    )
    address = models.CharField(max_length=150, verbose_name="Адрес")
    site = models.CharField(max_length=100, verbose_name="Веб-сайт")
    contacts = models.CharField(max_length=15, verbose_name="Контактный телефон")

    def __str__(self):
        return self.title


class Specializations(models.Model):
    title = models.CharField(max_length=100, verbose_name="Специализация ресторана")

    def __str__(self):
        return self.title
