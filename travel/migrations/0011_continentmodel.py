# Generated by Django 2.2 on 2023-12-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_registerationmodel_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
