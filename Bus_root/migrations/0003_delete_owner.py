# Generated by Django 5.1.1 on 2024-12-14 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bus_root', '0002_alter_movieinfo_bus_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
