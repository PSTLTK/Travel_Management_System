# Generated by Django 2.2 on 2023-12-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0025_bookingmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='booked_at',
            field=models.DateTimeField(default=None),
        ),
    ]
