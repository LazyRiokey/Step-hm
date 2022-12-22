from django.db import models

# Create your models here.


class Complaints(models.Model):

    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    e_mail = models.EmailField(verbose_name="E-mail")
    contacts = models.CharField(max_length=12, verbose_name="Контактный телефон")
    product_name = models.CharField(max_length=100, verbose_name="Название товара")
    purchase_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="Дата покупки"
    )
    problem_description = models.CharField(
        max_length=500, verbose_name="Описание проблемы"
    )
