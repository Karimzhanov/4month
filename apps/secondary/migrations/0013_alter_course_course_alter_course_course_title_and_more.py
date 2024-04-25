# Generated by Django 5.0.4 on 2024-04-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0012_course_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(max_length=255, verbose_name='курс '),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=255, verbose_name='заголовка курса '),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='info_user/', verbose_name='Фотография курса '),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(verbose_name='Цена курса '),
        ),
    ]
