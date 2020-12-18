import json
import re

from django.db import models
# from PIL import Image
from functions import sendSqs
from functions.async_services import sendQueue_async
from user_extended.models import Extension


class Seller(models.Model):
    user_extension = models.OneToOneField(Extension, on_delete=models.CASCADE,
                                          verbose_name='Associated user',
                                          related_name='seller')

    def __str__(self):
        return "seller: %s" % self.user_extension.user.username

    def getSellerPathForImage(self):
        return "%d_%s_from_%s" % (
                self.pk, self.user_extension.user.username, self.user_extension.city
        )


class Apartment(models.Model):
    owner = models.ForeignKey(Seller, on_delete=models.CASCADE,
                              verbose_name='Seller/Owner of apartment',
                              default=None)
    title = models.CharField(max_length=30, blank=False, default=None)
    description = models.TextField(default=None)
    price = models.PositiveIntegerField(blank=False, default=None)
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


def uploadTo(self, filename):
    path = self.getSellerPathForImage()
    filepath = 'apartment_images/%s/%s' % (
            path, filename
    )

    return filepath


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

    def save(self):
        super().save()
        obj_name = self.get_image_amazon_path()
        msg = json.dumps({
                'filename': obj_name,
                'size':     400,
        })

        sendQueue_async(msg, sendSqs.RESIZE_NAME, sendSqs.RESIZE_ATTR)

        # if obj_name:
        #     main(obj_name)

        # img = Image.open(self.image.path)
        #
        # if img.height > 400 or img.width > 300:
        #     img.thumbnail((400, 300))
        #     img.save(self.image.path)

    def get_image_amazon_path(self):
        path_name = re.search(r'/(.+)\?', self.image.url).group(1)

        if 'default_image/apartment.jpeg' in path_name:
            return False

        last_occurrence = path_name.rfind('/')

        if last_occurrence == -1:
            return path_name

        file_name = path_name[last_occurrence+1:]

        obj_name_in_bucket = uploadTo(self, file_name)

        print(f'obj_name_in_bucket: {file_name}')

        return obj_name_in_bucket

