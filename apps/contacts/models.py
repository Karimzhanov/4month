from django.db import models

# Create your models here.
class Contacts(models.Model):
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Номер телефона "
    )

    our_location  = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )


    email = models.EmailField(
        max_length=255,
        verbose_name="Почта "
   
    )

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = " Контакты"
