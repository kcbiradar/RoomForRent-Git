# Generated by Django 4.0 on 2022-01-27 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room_room_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
    ]