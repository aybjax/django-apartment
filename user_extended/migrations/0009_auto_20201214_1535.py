# Generated by Django 3.1.4 on 2020-12-14 15:35

from django.db import migrations, models
import user_extended


class Migration(migrations.Migration):

    dependencies = [
        ('user_extended', '0008_auto_20201213_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='image',
            field=models.ImageField(default='default_image/default.jpeg', upload_to=user_extended.models.uploadTo),
        ),
    ]
