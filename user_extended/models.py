from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from . import constants
from user_extended.functions.uploadTo import uploadTo


class Extension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Associated user',
                                null=True, blank=False, related_name='user_extension')
    city = models.CharField(max_length=2,
                            choices=constants.PROFILE_CITY,
                            default=constants.PROFILE_CITY_DEFAULT_VALUE)
    image = models.ImageField(upload_to=uploadTo, default='default_image/default.gif')

    def __str__(self):
        return "%s from %s" % (self.user.username, self.get_city_display())

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 250 or img.width > 200:
    #         img.thumbnail((200, 250))
    #         img.save(self.image.path)
