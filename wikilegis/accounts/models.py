from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from accounts.managers import UserManager


class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        null=True,
        blank=True,
        help_text=_('Requerido. 150 caracteres o menos. Letras,  '
                    'dígitos y @/./+/-/_ solamente.')
    )
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        if self.first_name and self.last_name:
            return ' '.join([self.first_name, self.last_name]).strip()
        elif self.first_name:
            return self.first_name
        else:
            return self.email.split('@')[0]
