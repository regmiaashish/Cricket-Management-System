# Generated by Django 5.1.4 on 2025-01-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_remove_coach_team_player_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='description',
            field=models.TextField(default='Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='batting_style',
            field=models.CharField(choices=[('Right Hand', 'right_hand'), ('Left Hand', 'left_hand')], default='Right hand', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='bowling_style',
            field=models.CharField(choices=[('Right Arm Fast', 'right_arm_fast'), ('Right Arm Medium', 'right_arm_medium'), ('Right Arm Off-Spin', 'right_arm_off_spin'), ('Left Arm Fast', 'left_arm_fast'), ('Left Arm Medium', 'left_arm_medium'), ('Left Arm Orthodox Spin', 'left_arm_orthodox_spin')], default='left Arm Medium', max_length=30),
        ),
    ]
