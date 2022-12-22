# Generated by Django 4.1.1 on 2022-09-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="mail",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="review",
            name="nickname",
            field=models.CharField(max_length=50, unique=True, verbose_name="Ник"),
        ),
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(verbose_name="Звёзды"),
        ),
    ]