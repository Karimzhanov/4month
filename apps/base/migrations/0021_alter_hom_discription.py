# Generated by Django 5.0.4 on 2024-04-18 14:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_secondary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hom',
            name='discription',
            field=ckeditor.fields.RichTextField(verbose_name='описания'),
        ),
    ]
