from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    # main atributes
    phone_number = models.CharField(max_length=20, help_text=_('User phone number'), unique=True)
    name = models.CharField(max_length=128, help_text=_('User name'))
    coins = models.PositiveIntegerField(default=0, help_text=_('User coins'))

    # user telegram info
    avatar = models.ImageField(upload_to='avatars/', help_text=_('User profile image'), blank=True, null=True)
    username = models.CharField(max_length=128, help_text=_('User telegram username'), blank=True, null=True)
    telegram_id = models.CharField(max_length=64, help_text=_('User telegram id'), null=True, blank=True)
    
    # permissions
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # other functions or atributes
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']
    
    
    
    def __str__(self) -> str:
        return self.phone_number
    