# Generated by Django 2.0.3 on 2018-03-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_camera_has_sound'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='owner_name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
