from django.contrib import admin
from src.oauth.models import User

from .models import Follower, UsersSocialLink


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'join_date', 'is_active', 'is_superuser')
    list_display_links = ('email',)

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'subsriber')

@admin.register(UsersSocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram_link', 'youtube_link', 'vk_link')