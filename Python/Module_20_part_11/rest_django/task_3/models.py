from django.db import models

# Create your models here.


class Poetry(models.Model):
    author = models.CharField(max_length=200, verbose_name="Автор")
    verse = models.TextField(blank=True, verbose_name="Стихотворение")
    verse_theme = models.ForeignKey(
        "VerseTheme", verbose_name="Тема", on_delete=models.PROTECT, null=True
    )

    def __str__(self):
        return self.author


class VerseTheme(models.Model):
    theme = models.CharField(max_length=150, verbose_name="Тема")

    def __str__(self):
        return self.theme
