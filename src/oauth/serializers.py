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

class SocialLinkSerializer(serializers.ModelSerializer):
    '''
    [CRUD] Сериализация социаильных сетей пользователя
    '''
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UsersSocialLink
        fields = ('id','link')

class AuthorSerializer(serializers.ModelSerializer):
    '''
    Сериализация профиля пользователя
    '''
    social_links = SocialLinkSerializer(many=True)

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
            'social_links',
        )

