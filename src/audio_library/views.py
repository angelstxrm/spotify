from rest_framework import generics
from .models import License, Genre, Album, Track, Comment, PlayList
from .serializers import LicenseSerializer, GenreSerializer, AlbumSerializer, TrackSerializer, CommentSerializer, PlayListSerializer

class GenreView(generics.ListAPIView):
    '''
    Получение списка жанров
    '''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer