from django.db import models

from seller_profile.models import Apartment
from user_extended.models import Extension


class Buyer(models.Model):
    user = models.OneToOneField(Extension, on_delete=models.CASCADE, null=True, blank=True)
    apartmentLiked = models.ForeignKey(Apartment, on_delete=models.SET_NULL,
                                       blank=True, null=True,
                                       related_name='likee')
    apartmentRenting = models.ForeignKey(Apartment, on_delete=models.SET_NULL,
                                         blank=True, null=True,
                                         related_name='renter')

    def __str__(self):
        return "buyer: %s from %s" % (self.user.user.username, self.user.get_city_display())
