# Generated by Django 2.2.1 on 2020-01-10 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='date',
            new_name='publicationDate',
        ),
    ]
