# Generated by Django 5.0.6 on 2024-06-15 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0005_follower_sociallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersSocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_link', models.URLField(blank=True, max_length=100, null=True, verbose_name='Ссылка на Telegram')),
                ('youtube_link', models.URLField(blank=True, max_length=100, null=True, verbose_name='Ссылка на YouTube')),
                ('vk_link', models.URLField(blank=True, max_length=100, null=True, verbose_name='Ссылка на Вконтакте')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.DeleteModel(
            name='SocialLink',
        ),
    ]
