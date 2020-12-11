from django.db import models

from apartment.models import Apartment
from user_extended.models import UserExtended


class Buyer(models.Model):
    user = models.OneToOneField(UserExtended, on_delete=models.CASCADE, null=True, blank=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "buyer: %s from %s" % (self.user.user.username, self.user.get_city_display())
