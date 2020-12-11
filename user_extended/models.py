from django.db import models
from django.contrib.auth.models import User
from . import constants


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Associated user')
    city = models.CharField(max_length=2, choices=constants.PROFILE_CITY, default=constants.PROFILE_CITY_DEFAULT_VALUE)
    image = models.ImageField(upload_to='profile_image', default='default_image/default.jpeg')

    def __str__(self):
        return "%s from %s" % (self.user.username, self.get_city_display())
