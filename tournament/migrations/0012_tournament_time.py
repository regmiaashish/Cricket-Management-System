# Generated by Django 5.1.4 on 2025-01-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0011_alter_coach_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='time',
            field=models.TimeField(default=0),
        ),
    ]
