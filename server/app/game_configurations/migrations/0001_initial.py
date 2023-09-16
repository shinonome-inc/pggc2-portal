# Generated by Django 4.2.5 on 2023-09-16 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, unique=True)),
                ('value', models.CharField(default='0', max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'configuration',
            },
        ),
    ]