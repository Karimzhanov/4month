# Generated by Django 5.0.4 on 2024-04-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='contact',
        ),
        migrations.AddField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
