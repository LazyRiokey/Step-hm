from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("random_verse/", RandomVerse.as_view()),
    path("random_verse_author/", RandomVerseAuthor.as_view()),
    path("random_verse_theme/", RandomVerseTheme.as_view()),
    path("all_verses_author/", AllVersesAuthor.as_view()),
    path("all_authors/", AllAuthors.as_view()),
    path("all_themes/", AllThemes.as_view()),
    path("all_verses_themes/", AllVersesTheme.as_view()),
]
