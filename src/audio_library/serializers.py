from rest_framework import serializers

from src.base.services import delete_old_file
from .models import Genre, License, Album

class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

class GenreSerializer(BaseSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class LicenseSerializer(BaseSerializer):
    class Meta:
        model = License
        fields = ('id', 'text')

class AlbumSerializer(BaseSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'description', 'cover', 'private')

        def update(self, instance, validated_data):
            delete_old_file(instance.cover.path)
            return super().update(instance, validated_data)