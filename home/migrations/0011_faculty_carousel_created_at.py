# Generated by Django 5.0.2 on 2024-05-29 16:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_contactus_subject_contactus_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='faculty/')),
                ('title_name', models.TextField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='carousel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
