# Generated by Django 2.2.1 on 2020-01-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200113_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book_pictures'),
        ),
    ]
