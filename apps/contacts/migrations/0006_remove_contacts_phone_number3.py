# Generated by Django 5.0.4 on 2024-04-17 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contacts_email1_contacts_phone_number1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='phone_number3',
        ),
    ]
