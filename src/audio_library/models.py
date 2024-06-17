from django.db import models
from src.base.services import (
    get_patch_upload_cover, 
    get_patch_upload_playlist, 
    get_patch_upload_track, 
    validate_size_image
)
from src.oauth.models import User
from django.core.validators import FileExtensionValidator


class License(models.Model):
    '''
    Модель лицензии треков пользователей
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='licenses'
    )
    text = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'


class Genre(models.Model):
    '''
    Модель жанра треков
    '''
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
    

class Album(models.Model):
    '''
    Модель альбома
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000)
    private = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to=get_patch_upload_cover, blank=True, null=True, validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png']
            ), validate_size_image
        ]
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Track(models.Model):
    '''
    Модель трека
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tracks'
    )
    title = models.CharField(max_length=100)
    license = models.ForeignKey(
        License, on_delete=models.PROTECT, related_name='license_tracks'
    )
    genre = models.ManyToManyField(Genre, related_name='genre_tracks')
    album = models.ForeignKey(
        Album, on_delete=models.SET_NULL, blank=True, null=True
    )
    link_of_author = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(
        upload_to=get_patch_upload_track,
        validators=[FileExtensionValidator(
            allowed_extensions=['mp3', 'wav']
        )], help_text='Поддерживается формат: mp3, wav',
    )
    create_at = models.DateTimeField(auto_now_add=True)
    plays_count = models.PositiveIntegerField(default=0)
    download_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    user_of_likes = models.ManyToManyField(User, related_name='likes_of_tracks')

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return f'{self.user} - {self.title}'
    
class Comment(models.Model):
    '''
    Модель комментария к треку
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='tracks_comments')
    text = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class PlayList(models.Model):
    '''
    Модель плейлиста пользователя
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    title = models.CharField(max_length=50)
    tracks = models.ManyToManyField(Track, related_name='track_playlists')
    playlist_photo = models.ImageField(
        upload_to=get_patch_upload_playlist, blank=True, null=True, validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png']
            ), validate_size_image
        ]
    )

    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'