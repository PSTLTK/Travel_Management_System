# Generated by Django 2.2 on 2023-12-22 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0037_auto_20231221_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingmodel',
            name='register',
        ),
    ]
