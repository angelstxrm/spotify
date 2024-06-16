from rest_framework import viewsets, parsers, permissions

from .models import User
from .serializers import UserProfileSerializer, AuthorSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    '''
    Просмотр и изменение данных пользователя 
    '''
    queryset = User.objects.all()
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
    
class AuthorView(viewsets.ReadOnlyModelViewSet):
    '''
    Список авторов
    '''
    queryset = User.objects.all()
    serializer_class = AuthorSerializer

