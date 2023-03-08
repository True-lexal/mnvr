from django.contrib.auth.models import AbstractUser
from django.db import models
from .validator import UnicodeUsernameValidatorNew
from django.utils.translation import gettext_lazy as _


class CustomUserStatus(models.Model):
    status_name = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class CustomUserGroup(models.Model):
    group_name = models.CharField(max_length=150, verbose_name='Группа')

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class CustomUsers(AbstractUser):
    username_validator = UnicodeUsernameValidatorNew()
    username = models.CharField(
        _("username"),
        max_length=100,
        unique=True,
        help_text=_(
            "Required. 100 characters or fewer. Letters, digits and - only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(verbose_name='Email', null=True, unique=True)
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', blank=True)
    status = models.ForeignKey(CustomUserStatus, on_delete=models.SET_NULL, verbose_name='Статус', null=True, default=1)
    group = models.ForeignKey(CustomUserGroup, on_delete=models.SET_NULL, verbose_name='Группа', null=True, default=1)
    is_confirmed = models.BooleanField(default=False, verbose_name='Подтвержден Email')

