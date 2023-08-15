# Generated by Django 4.2.4 on 2023-08-15 09:58

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=mapbox_location_field.models.LocationField(blank=True, map_attrs={}, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='location',
            field=mapbox_location_field.models.LocationField(blank=True, map_attrs={}, null=True),
        ),
    ]