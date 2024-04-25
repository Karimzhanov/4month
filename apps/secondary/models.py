from django.db import models

# Create your models here.
class Course(models.Model):

    image = models.ImageField(
        upload_to="info_user/",
        verbose_name="Фотография курса "
    )

    course = models.CharField(
        max_length=255,
        verbose_name= "курс "
    )

    course_title = models.CharField(
        max_length=255,
        verbose_name="заголовка курса "
    )



    def __str__(self):
        return self.course

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = " Курсы"
