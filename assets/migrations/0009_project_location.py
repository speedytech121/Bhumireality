# Generated by Django 5.0.2 on 2024-05-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_infratech_infratechimages_remove_project_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.ImageField(blank=True, null=True, upload_to='project/location/'),
        ),
    ]
