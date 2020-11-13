from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import DateTimeField

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if email is None:
            raise ValueError('Email address must be set.')
        if username is None:
            raise ValueError('Username must be set.')
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        if password is None:
            raise ValueError('Password must be set.')
        user = self.create_user(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = CharField(
        'Адрес электронной почты',
        max_length=255,
        unique=True,
        db_index=True
    )
    username = CharField(
        'Имя пользователя',
        max_length=64,
        unique=True,
        db_index=True
    )
    is_active = BooleanField(
        'Активирован',
        default=True
    )
    is_staff = BooleanField(
        'Персонал',
        default=False
    )
    is_superuser = BooleanField(
        'Суперпользователь',
        default=False
    )
    created_at = DateTimeField(
        'Создан',
        auto_now_add=True
    )
    updated_at = DateTimeField(
        'Обновлён',
        auto_now=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        ordering = ['-email', '-username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def tokens(self):
        refresh_token = RefreshToken.for_user(self)
        return {'refresh': '{}'.format(refresh_token), 'access': '{}'.format(refresh_token.access_token)}

    def __str__(self):
        return '{}'.format(self.email)