# Generated by Django 5.0.6 on 2024-05-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
