from django.db import models
from user_extended.models import Extension
from .functions.uploadTo import uploadTo


class Seller(models.Model):
    user = models.OneToOneField(Extension, on_delete=models.CASCADE,
                                verbose_name='Associated user',
                                related_name='seller')

    def __str__(self):
        return "seller: %s" % self.user.user.username

    def getSellerPathForImage(self):
        return "%d_%s_from_%s" % (
                self.pk, self.user.user.username, self.user.city
        )


class Apartment(models.Model):
    owner = models.ForeignKey(Seller, on_delete=models.CASCADE,
                              verbose_name='Seller/Owner of apartment',
                              default=None)
    street = models.CharField(max_length=50, blank=False, default=None)
    home = models.PositiveSmallIntegerField(blank=False, default=None)
    apartment = models.PositiveSmallIntegerField(blank=False, default=None)

    def __str__(self):
        return "%s street, %d, apt# %d of %s" % (
                self.street, self.home, self.apartment, self.owner
        )

    def getSellerPathForImage(self):
        return '%s/apt_%s_%d_%d' % (
                self.owner.getSellerPathForImage(),
                self.street,
                self.home,
                self.apartment,
        )


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE,
                                  related_name="images")
    image = models.ImageField(
        upload_to=uploadTo,
        default='default_image/apartment.jpeg',
    )

    def __str__(self):
        return 'apartment: %s of %s' % (
                self.apartment, self.apartment.owner
        )

    def getSellerPathForImage(self):
        return self.apartment.getSellerPathForImage()
