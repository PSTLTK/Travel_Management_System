# Generated by Django 2.2 on 2023-12-06 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_registerationmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerationmodel',
            name='acc_name',
        ),
        migrations.RemoveField(
            model_name='registerationmodel',
            name='name',
        ),
    ]
