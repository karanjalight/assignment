# Generated by Django 4.1.3 on 2022-11-06 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_parks_trails_water_delete_places'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='parks',
            new_name='park',
        ),
        migrations.RenameModel(
            old_name='trails',
            new_name='trail',
        ),
    ]
