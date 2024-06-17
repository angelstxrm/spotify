# Generated by Django 5.0.6 on 2024-06-17 16:56

import django.core.validators
import django.db.models.deletion
import src.base.services
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('private', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=src.base.services.get_patch_upload_cover, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), src.base.services.validate_size_image])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licenses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link_of_author', models.CharField(blank=True, max_length=500, null=True)),
                ('file', models.FileField(help_text='Поддерживается формат: mp3, wav', upload_to=src.base.services.get_patch_upload_track, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('plays_count', models.PositiveIntegerField(default=0)),
                ('download_count', models.PositiveIntegerField(default=0)),
                ('likes_count', models.PositiveIntegerField(default=0)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='audio_library.album')),
                ('genre', models.ManyToManyField(related_name='genre_tracks', to='audio_library.genre')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='license_tracks', to='audio_library.license')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to=settings.AUTH_USER_MODEL)),
                ('user_of_likes', models.ManyToManyField(related_name='likes_of_tracks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
            },
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('playlist_photo', models.ImageField(blank=True, null=True, upload_to=src.base.services.get_patch_upload_playlist, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), src.base.services.validate_size_image])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL)),
                ('tracks', models.ManyToManyField(related_name='track_playlists', to='audio_library.track')),
            ],
            options={
                'verbose_name': 'Плейлист',
                'verbose_name_plural': 'Плейлисты',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks_comments', to='audio_library.track')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
