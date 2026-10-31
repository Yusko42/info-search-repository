from django.db import models

# Create your models here.
class University(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное название")
    short_name = models.CharField(max_length=63, verbose_name="Сокращённое название")
    founded_date = models.DateField(verbose_name="Дата создания")

    def __str__(self):
        return self.short_name

class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        verbose_name="Университет",
    )
    enrollment_year = models.IntegerField(verbose_name="Год поступления")

    def __str__(self):
        return self.full_name