from django.db import models

# Create your models here.
class Course(models.Model):

    image1 = models.ImageField(
        upload_to="info_user/",
        verbose_name="Фотография курса 1"
    )

    course1 = models.CharField(
        max_length=255,
        verbose_name= "курс 1"
    )

    course_title1 = models.CharField(
        max_length=255,
        verbose_name="заголовка курса 1"
    )

    price1 = models.IntegerField(
        verbose_name= "Цена курса 1"

    )

   
   
    def __str__(self):
        return self.course1

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = " Курсы"
