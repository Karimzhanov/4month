# Generated by Django 5.0.4 on 2024-04-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_course_image1_course_image2_course_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image1',
            field=models.ImageField(upload_to='info_user/', verbose_name='Фотография курса 1'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image2',
            field=models.ImageField(upload_to='info_user/', verbose_name='Фотография курса 2'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image3',
            field=models.ImageField(upload_to='info_user/', verbose_name='Фотография курса 3'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image4',
            field=models.ImageField(upload_to='info_user/', verbose_name='Фотография курса 4'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image5',
            field=models.ImageField(upload_to='info_user/', verbose_name='Фотография курса 5'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image6',
            field=models.ImageField(upload_to='info_user/', verbose_name='Фотография курса 6'),
        ),
    ]