from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .models import Poetry

# Create your views here.


class RandomVerse(APIView):
    def get(self, request):
        counter = Poetry.objects.count()
        random_object = Poetry.objects.get(id=random.randint(0, counter - 1)).verse
        return Response({"verses": random_object})


class RandomVerseAuthor(APIView):
    def post(self, request):
        author = request.data["author"]
        obj = Poetry.objects.filter(author=author)[
            random.randint(0, Poetry.objects.filter(author=author).count() - 1)
        ]
        return Response({"verse": obj.verse})


class RandomVerseTheme(APIView):
    def post(self, request):
        theme = request.data["verse_theme_id"]
        obj = Poetry.objects.filter(verse_theme_id=theme)[
            random.randint(0, Poetry.objects.filter(verse_theme_id=theme).count() - 1)
        ]
        return Response({"verse": obj.verse, "verse_theme": obj.verse_theme_id})


class AllVersesAuthor(APIView):
    def post(self, request):
        author = request.data["author"]
        obj = Poetry.objects.filter(author=author)
        return Response({"verse": obj.all().values("verse")})


class AllAuthors(APIView):
    def get(self, request):
        queryset = Poetry.objects.values("author").distinct()
        return Response({"authors": queryset})


class AllThemes(APIView):
    def get(self, request):
        queryset = Poetry.objects.values("verse_theme").distinct()
        return Response({"themes": queryset})


class AllVersesTheme(APIView):
    def post(self, request):
        theme = request.data["verse_theme"]
        obj = Poetry.objects.filter(verse_theme=theme)
        return Response({"verse": obj.all().values("verse")})
