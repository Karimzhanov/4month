# Generated by Django 5.0.4 on 2024-04-22 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0014_merge_20240418_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_duration',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
    ]
