from django.db import models
from django.urls import reverse
# Create your models here.


class People(models.Model):

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    city = models.CharField(max_length=50, verbose_name="Город")

    # def get_absolute_url(self):
    #     return reverse("find_people", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
