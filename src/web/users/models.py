from django.contrib.auth.base_user import AbstractBaseUser
from django.core import validators, urlresolvers
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
import django.contrib.auth.models as auth_models

from drapo.common import generate_random_secret_string


class UserManager(auth_models.UserManager):
    pass


# See the django.contrib.auth.models.User for details
# We need to copy it here for enlarge username, first_name and last_name's lengths from 30 to 100 characters
class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w\d.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # Custom drapo users methods
    @property
    def is_email_confirmed(self):
        try:
            return self.email_confirmation.confirmed
        except EmailConfirmation.DoesNotExist:
            return True

    def get_absolute_url(self):
        return urlresolvers.reverse('users:profile', args=[self.id])


class EmailConfirmation(models.Model):
    user = models.OneToOneField(User, related_name='email_confirmation')

    token = models.CharField(max_length=32, default=generate_random_secret_string)

    confirmed = models.BooleanField(default=False)

    def send(self):
        self.user.email_user('Email confirmation', 'You confirmation token is ' + self.token)
