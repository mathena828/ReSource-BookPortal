# Generated by Django 2.2.1 on 2020-01-12 18:04

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
