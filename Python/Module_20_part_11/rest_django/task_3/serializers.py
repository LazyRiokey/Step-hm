from rest_framework import serializers

from .models import Poetry


class PoetrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Poetry
        fields = ["id" ,"author", "verse", "verse_theme"]