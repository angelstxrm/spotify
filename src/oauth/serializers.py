from rest_framework import serializers

from .models import User, Follower, UsersSocialLink

class UserProfileSerializer(serializers.ModelSerializer):
    '''
    Сериализация профиля пользователя
    '''
    class Meta:
        model = User
        fields = (
            'username',
            'join_date',
            'country',
            'city',
            'bio',
            'display_name',
            'avatar',
        )

class AuthorSerializer(serializers.ModelSerializer):
    '''
    Сериализация профиля пользователя
    '''
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'join_date',
            'country',
            'city',
            'bio',
            'display_name',
            'avatar',
        )

class SocialLinkSerializer(serializers.ModelSerializer):
    '''
    [CRUD] Сериализация социаильных сетей пользователя
    '''
    class Meta:
        model = UsersSocialLink
        fields = ('link',)