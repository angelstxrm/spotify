# Generated by Django 5.0.6 on 2024-06-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0006_userssociallink_delete_sociallink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userssociallink',
            name='telegram_link',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='Ссылка на Telegram'),
        ),
        migrations.AlterField(
            model_name='userssociallink',
            name='vk_link',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='Ссылка на Вконтакте'),
        ),
        migrations.AlterField(
            model_name='userssociallink',
            name='youtube_link',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='Ссылка на YouTube'),
        ),
    ]