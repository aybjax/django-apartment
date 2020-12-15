# Generated by Django 3.1.4 on 2020-12-14 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_extended', '0009_auto_20201214_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_extension', to=settings.AUTH_USER_MODEL, verbose_name='Associated user'),
        ),
    ]
