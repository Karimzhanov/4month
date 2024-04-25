from django.db import models
from ckeditor.fields import RichTextField


class Home(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Главная страница"
    )


    the_background = models.ImageField(
        upload_to= "info_users",
        verbose_name= "Задний Фон"
    )

    image = models.ImageField(
        upload_to="info_users/",
        verbose_name="Фотография  загловка"
    )

   

    discription = models.TextField(
        max_length=255,
        verbose_name="описания заговка"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = " Главная страницы"

class About(models.Model):
    about = models.CharField(
        max_length=255,
        verbose_name="О нас"
    )

    name = models.CharField(
        max_length=255,
        verbose_name="Ф.И.О",
        default="Введите Ф.И.О рукаводителя " 
    )

    image = models.ImageField(
        upload_to="info_user/",
        verbose_name="Фотография руководителя"
    )

    email = models.EmailField(
        max_length=255,
        verbose_name="Почта руководителя"
    )

    phone_number = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )

    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = " О нас"


        
class Secondary(models.Model):
    online = models.IntegerField(
        verbose_name = "Наш онлайн-курс"
    )

    image = models.ImageField(
        upload_to="info_user/",
        verbose_name="Фото заднего фона"
    )
    Academic_programs = models.IntegerField(
        verbose_name = "Академические программы"
    )
    Certified_Students = models.IntegerField(
        verbose_name = "Сертифицированные студенты"
    )
    Enrolled_Students = models.IntegerField(
        verbose_name = "Зачисленные студенты"
    )
    def __str__(self):
        return str(self.online)

    class Meta:
        verbose_name = "Доп информации"
        verbose_name_plural = "Доп информации"
   
class Hom(models.Model):
    image = models.ImageField(
        upload_to="info_user1/",
        verbose_name="Фотография Описание"
    )

    
    discription = RichTextField(
        verbose_name="описания"
    )

    
    discriptions = models.TextField(
        verbose_name="описания заговка 1"
    )

    discriptions1 = models.CharField(
        max_length=255,
        verbose_name="короткое описания 1"
    )
    discriptions2 = models.CharField(
        max_length=255,
        verbose_name="короткое описания 2"
    )


    discriptions3 = models.CharField(
        max_length=255,
        verbose_name="короткое описания 3"
    )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = "Описания  курсов"
        verbose_name_plural = " Описания курсов"