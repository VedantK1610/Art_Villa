# Generated by Django 4.2.1 on 2023-05-25 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_photo_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
