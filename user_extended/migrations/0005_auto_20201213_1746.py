# Generated by Django 3.1.4 on 2020-12-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_extended', '0004_auto_20201213_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='city',
            field=models.CharField(choices=[('qr', 'qarafandi'), ('as', 'astana'), ('al', 'almaty'), ('jz', 'jezqazfan'), ('mx', 'mvxosranskh')], default='as', max_length=2),
        ),
    ]
