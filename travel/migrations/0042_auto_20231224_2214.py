# Generated by Django 2.2 on 2023-12-24 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0041_auto_20231224_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinationmodel',
            name='adult_per_day',
        ),
        migrations.RemoveField(
            model_name='destinationmodel',
            name='child_per_day',
        ),
    ]
