# Generated by Django 3.1.4 on 2020-12-14 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller_profile', '0006_auto_20201214_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='user',
            new_name='user_extension',
        ),
    ]