from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from users.manager import UserManager

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractUser):
    username = None

    login = models.CharField(max_length=505, verbose_name='Логин')
    password = models.CharField(max_length=505, verbose_name='Пароль')
    email = models.EmailField(unique=True, verbose_name='Электронная почта пользователя')
    phone = models.CharField(max_length=500, verbose_name='Номер телефона', **NULLABLE)
    birth_day = models.DateField(verbose_name='Дата рождения')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    edited_at = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')
    email_verify = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

