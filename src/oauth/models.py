from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from src.base.services import validate_size_image
from src.oauth.managers import CustomUserManager



class User(AbstractUser):
    '''
    Кастомная модель пользователя
    '''
    username = models.CharField(
        'Username', max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField('Email', max_length=100, unique=True)
    join_date = models.DateField('Join Date', auto_now_add=True)
    country = models.CharField(
        'Country', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100, blank=True, null=True
    )
    bio = models.TextField('Bio', blank=True, null=True)
    display_name = models.CharField(
        'Display Name', max_length=100, blank=True, null=True
    )
    avatar = models.ImageField(
        'Avatar', upload_to='oauth/avatars/', help_text='Поддерживается формат: jpg, jpeg, png', blank=True, null=True, validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png']
            ), validate_size_image
        ]
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
    
class Follower(models.Model):
    '''
    Кто друг на друга подписан
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner'
    )
    subsriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subsribers'
    )

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return f'{self.subsriber} подписан на {self.user}'
    
class UsersSocialLink(models.Model):
    '''
    Социальные сети пользователя
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='social_links'
    )
    link = models.URLField(
        'Ссылка на соц.сети', max_length=100, blank=True, null=True, unique=True
    )

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'