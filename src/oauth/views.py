from rest_framework import viewsets, parsers, permissions

from src.base.permissions import IsAuthor
from .models import UsersSocialLink

from .models import User
from . import serializers

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
    
class AuthorView(viewsets.ReadOnlyModelViewSet):
    '''
    Список авторов
    '''
    queryset = User.objects.all()
    serializer_class = serializers.AuthorSerializer


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