# Generated by Django 5.1.4 on 2025-01-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_coach'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='team',
        ),
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='player_images/'),
        ),
    ]
