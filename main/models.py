from django.db import models

# 1. Create your models here.
# 2. Create migrations: python manage.py makemigrations
# 3. Migrate: python manage.py migrate


class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    is_activated = models.BooleanField(verbose_name='Активация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год')

    def __str__(self):
        return ' '.join([str(self.brand), str(self.model)])

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Client(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=30, verbose_name='Город')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Эл. почта')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return ' '.join([self.name, self.last_name])
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'