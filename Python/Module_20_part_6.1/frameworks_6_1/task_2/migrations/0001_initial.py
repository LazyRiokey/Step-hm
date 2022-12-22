# Generated by Django 4.1.2 on 2022-10-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Complaints",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_name", models.CharField(max_length=50, verbose_name="Фамилия")),
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("e_mail", models.EmailField(max_length=254, verbose_name="E-mail")),
                (
                    "contacts",
                    models.CharField(max_length=12, verbose_name="Контактный телефон"),
                ),
                (
                    "product_name",
                    models.CharField(max_length=100, verbose_name="Название товара"),
                ),
                ("purchase_date", models.DateField(verbose_name="Дата покупки")),
                (
                    "problem_description",
                    models.CharField(max_length=500, verbose_name="Описание проблемы"),
                ),
            ],
        ),
    ]
