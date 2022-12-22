from django.db import models

# Create your models here.


class Сritique(models.Model):

    nickname = models.CharField(unique=True ,max_length=50, verbose_name="Ник")
    rating = models.SmallIntegerField(verbose_name="Рейтинг")
    review = models.TextField(max_length=500, verbose_name="Рецензия на книгу")
    spoilers = models.BooleanField(verbose_name="Содержит спойлеры?", default=False)

    def __str__(self):
        return self.nickname
