from django.db import models

# Create your models here.


class Review(models.Model):

    nickname = models.CharField(unique=True ,max_length=50, verbose_name="Ник")
    mail = models.EmailField(unique=True ,verbose_name="Email")
    stars = models.IntegerField(verbose_name="Звёзды")
    review = models.TextField(max_length=500, verbose_name="Опыт использования")

    def __str__(self):
        return self.nickname
