# Generated by Django 4.1.1 on 2022-09-22 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VerseTheme",
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
                ("theme", models.CharField(max_length=150, verbose_name="Тема")),
            ],
        ),
        migrations.CreateModel(
            name="Poetry",
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
                ("author", models.CharField(max_length=200, verbose_name="Автор")),
                ("verse", models.TextField(blank=True, verbose_name="Стихотворение")),
                (
                    "verse_theme",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="task_3.versetheme",
                        verbose_name="Тема",
                    ),
                ),
            ],
        ),
    ]
