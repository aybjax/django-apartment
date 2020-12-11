from django.contrib.auth.models import User
from django.db import models
from seller_profile import models as seller_models


class Apartment(models.Model):
    owner = models.ForeignKey(seller_models.Seller, on_delete=models.CASCADE,
                              verbose_name='Seller/Owner of apartment',
                              default=None)
    street = models.CharField(max_length=50, blank=False, default=None)
    home = models.PositiveSmallIntegerField(blank=False, default=None)
    apartment = models.PositiveSmallIntegerField(blank=False, default=None)

    def __str__(self):
        return "%s street, %d, apt# %d, belongs to %s" % (
                self.street, self.home, self.apartment, self.owner
        )
