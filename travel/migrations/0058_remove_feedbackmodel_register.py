# Generated by Django 2.2 on 2023-12-28 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0057_auto_20231227_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='register',
        ),
    ]
