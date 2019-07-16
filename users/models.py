from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _   # 做多國語言用


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
