import json
import re

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from functions import sendSqs
from functions.async_services import sendQueue_async
from . import constants


def uploadTo(self, filename):
    return "profile_image/%d_%s/%s" % (
            self.user.pk, self.user.username, filename
    )


class Extension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Associated user',
                                null=True, blank=False, related_name='user_extension')
    city = models.CharField(max_length=2,
                            choices=constants.PROFILE_CITY,
                            default=constants.PROFILE_CITY_DEFAULT_VALUE)
    image = models.ImageField(upload_to=uploadTo, default='default_image/default.gif')

    def __str__(self):
        return "%s from %s" % (self.user.username, self.get_city_display())

    def save(self):
        super().save()
        obj_name = self.get_image_amazon_path()
        msg = json.dumps({
                'filename': obj_name,
                'size':     250,
        })
        sendQueue_async(msg, sendSqs.RESIZE_NAME, sendSqs.RESIZE_ATTR)
        print("sendQueue")
        # if obj_name:
        #     main(obj_name) # commented for using bucket without lambda
        # img = Image.open(self.image.path)
        
        # if img.height > 250 or img.width > 200:
        #     img.thumbnail((200, 250))
        #     img.save(self.image.path)

    def get_image_amazon_path(self):
        path_name = re.search(r'/(.+)\?', self.image.url).group(1)

        if 'default_image/default.gif' in path_name:
            return False

        last_occurrence = path_name.rfind('/')

        if last_occurrence == -1:
            return path_name

        file_name = path_name[last_occurrence+1:]

        obj_name_in_bucket = uploadTo(self, file_name)

        print(f'obj_name_in_bucket: {file_name}')

        return obj_name_in_bucket
