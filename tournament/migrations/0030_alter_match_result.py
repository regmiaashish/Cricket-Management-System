# Generated by Django 5.1.4 on 2025-02-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0029_rename_team_1_score_match_ncc_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(blank=True, choices=[('NCC Wins', 'ncc'), ('Team 2 Wins', 'team_2'), ('Draw', 'draw')], max_length=20, null=True),
        ),
    ]
