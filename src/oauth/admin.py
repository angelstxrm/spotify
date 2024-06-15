from django.contrib import admin
from src.oauth.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'join_date', 'is_active', 'is_superuser')
    list_display_links = ('email',)



