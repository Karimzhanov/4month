# Generated by Django 5.0.4 on 2024-04-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0011_rename_course1_course_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_duration',
            field=models.CharField(default=1, max_length=255, verbose_name='Длительность курса'),
            preserve_default=False,
        ),
    ]
