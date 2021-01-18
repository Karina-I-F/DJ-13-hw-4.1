from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, serialize=False)
    name = models.CharField(max_length=64, blank=False, verbose_name='Модель телефона')
    price = models.FloatField(blank=True, verbose_name='Цена')
    image = models.URLField(blank=True, verbose_name='Изображение')
    release_date = models.DateField(blank=True, verbose_name='Дата релиза')
    lte_exists = models.BooleanField(blank=True)
    slug = models.SlugField(max_length=64, blank=True, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'телефон'
        verbose_name_plural = 'Телефон'
