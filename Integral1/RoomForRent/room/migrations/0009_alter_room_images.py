# Generated by Django 4.0 on 2022-01-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_alter_room_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='images',
            field=models.URLField(blank=True, max_length=264, null=True),
        ),
    ]