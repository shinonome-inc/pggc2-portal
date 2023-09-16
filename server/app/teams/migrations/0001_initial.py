# Generated by Django 4.2.5 on 2023-09-15 15:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='role')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
            ],
            options={
                'verbose_name_plural': 'Team Role',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='teamname')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='role', to='teams.teamrole')),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
    ]