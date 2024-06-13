from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from src.base.services import validate_size_image
from src.oauth.managers import CustomUserManager


class User(AbstractUser):
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
        'Avatar', upload_to='avatars/', blank=True, null=True, validators=[
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