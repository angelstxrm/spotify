from rest_framework import viewsets, parsers, permissions
from drf_yasg.utils import swagger_auto_schema
from src.base.permissions import IsAuthor
from .models import UsersSocialLink
from django.utils.decorators import method_decorator

from .models import User
from . import serializers


@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['Профиль пользователя']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['Профиль пользователя']))

class UserProfileViewSet(viewsets.ModelViewSet):
    '''
    Просмотр и изменение данных пользователя 
    '''
    queryset = User.objects.all()
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

  
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Авторы исполнений']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['Авторы исполнений']))

class AuthorView(viewsets.ReadOnlyModelViewSet):
    '''
    Список авторов
    '''
    queryset = User.objects.all().prefetch_related('social_links')
    serializer_class = serializers.AuthorSerializer

@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Социальные сети']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['Социальные сети']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['Социальные сети']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['Социальные сети']))

class SocialLinkViewSet(viewsets.ModelViewSet):
    '''
    [CRUD] Социальные сети пользователя
    '''
    serializer_class = serializers.SocialLinkSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.request.user.social_links.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)