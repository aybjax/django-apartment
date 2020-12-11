# Generated by Django 3.1.4 on 2020-12-11 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('qr', 'qarafandi'), ('as', 'astana'), ('al', 'almaty'), ('jz', 'jezqazfan'), ('mx', 'mvxosranskh')], default='qr', max_length=2)),
                ('image', models.ImageField(default='default_image/default.jpeg', upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Associated user')),
            ],
        ),
    ]
