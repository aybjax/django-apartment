from django.db import models
from user_extended.models import Extension


class Seller(models.Model):
    user = models.OneToOneField(Extension, on_delete=models.CASCADE,
                                verbose_name='Associated user',
                                related_name='seller')

    def __str__(self):
        return "seller: %s from %s" % (self.user.user.username, self.user.get_city_display())

    def getSellerPathForImage(self):
        return "%d_%s_%s" % (
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
        return "%s street, %d, apt# %d" % (
                self.street, self.home, self.apartment
        )

    def getSellerPathForImage(self):
        return self.owner.getSellerPathForImage()


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE,
                                  related_name="images")
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        try:
            image = self.image.url
        except:
            image = "no"
        return f'image: id = %d, of apartment: %s ||||| url: %s' % (
                self.pk, self.apartment, image
        )

    def getSellerPathForImage(self):
        self.apartment.getSellerPathForImage()
