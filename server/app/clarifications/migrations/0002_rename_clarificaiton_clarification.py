# Generated by Django 4.2.5 on 2023-09-16 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('problems', '0003_rename_points_difficulty_point'),
        ('clarifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clarificaiton',
            new_name='Clarification',
        ),
    ]
