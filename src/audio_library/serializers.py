from rest_framework import serializers
from .models import License, Genre, Album, Track, Comment, PlayList

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)