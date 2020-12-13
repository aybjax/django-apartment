from django.contrib.auth.models import User
from django.db.models.signals import post_save
from user_extended.models import Extension
from django.dispatch import receiver
from .models import Buyer


@receiver(post_save, sender=Extension)
def createBuyer(sender, instance, created, **kwargs):
    if created:
        buyer = Buyer.objects.create(user=instance)
        buyer.save()
