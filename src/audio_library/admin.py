from django.contrib import admin
from .models import Track, Album, Genre, License, Comment, PlayList


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('user',)
    list_filter = ('user',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name')
    list_display_links = ('user',)
    list_filter = ('user',)

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'create_at')
    list_display_links = ('user',)
    list_filter = ('genre', 'create_at')
    search_fields = ('user', 'genre__name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'track')
    list_display_links = ('user',)

@admin.register(PlayList)
class PlayList(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    list_display_links = ('user',)
    search_fields = ('user', 'tracks__title')