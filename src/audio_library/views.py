from rest_framework import generics, viewsets
from rest_framework import parsers
from src.base.services import delete_old_file
from src.base.permissions import IsAuthor
from .models import License, Genre, Album, Track, Comment, PlayList
from .serializers import GenreSerializer, LicenseSerializer, AlbumSerializer
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator


@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Жанры']))
class GenreView(generics.ListAPIView):
    '''
    Получение списка жанров
    '''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Лицензия автора']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['Лицензия автора']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['Лицензия автора']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['Лицензия автора']))
class LicenseViewSets(viewsets.ModelViewSet):
    '''
    [CRUD] Лицензии автора
    '''
    serializer_class = LicenseSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return License.objects.none()

        return License.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        if not getattr(self, 'swagger_fake_view', False):
            return serializer.save(user=self.request.user)

@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Альбомы']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['Альбомы']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['Альбомы']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['Альбомы']))        
class AlbumViewSets(viewsets.ModelViewSet):
    '''
    [CRUD] Альбомы
    '''
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Album.objects.none()

        return Album.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        if not getattr(self, 'swagger_fake_view', False):
            return serializer.save(user=self.request.user)
        
    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()