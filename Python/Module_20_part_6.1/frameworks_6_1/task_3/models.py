from django.db import models

# Create your models here.


class Goods(models.Model):

    title = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.SmallIntegerField(verbose_name="Цена")
    quantity = models.SmallIntegerField(verbose_name="Количество на складе")
    category = models.ForeignKey(
        "Category", verbose_name=("Категория"), on_delete=models.PROTECT
    )


class Category(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
