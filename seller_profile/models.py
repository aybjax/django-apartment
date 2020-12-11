from django.db import models

from user_extended import constants
from user_extended.models import UserExtended


class Seller(models.Model):
    user = models.OneToOneField(UserExtended, on_delete=models.CASCADE, verbose_name='Associated user')

    def __str__(self):
        return "seller: %s from %s" % (self.user.user.username, self.user.get_city_display())
