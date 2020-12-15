# Generated by Django 3.1.4 on 2020-12-14 15:35

from django.db import migrations, models
import seller_profile.functions.uploadTo


class Migration(migrations.Migration):

    dependencies = [
        ('seller_profile', '0005_auto_20201213_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='price',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='title',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='apartmentimage',
            name='image',
            field=models.ImageField(default='default_image/apartment.jpeg', upload_to=seller_profile.functions.uploadTo.uploadTo),
        ),
    ]
