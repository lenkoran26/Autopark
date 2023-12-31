from django.db import models
from django.urls import reverse

# 1. Create your models here.
# 2. Create migrations: python manage.py makemigrations
# 3. Migrate: python manage.py migrate


class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    is_activated = models.BooleanField(verbose_name='Активация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


# class Car(models.Model):
#     brand = models.CharField(max_length=30, verbose_name='Марка')
#     model = models.CharField(max_length=30, verbose_name='Модель')
#     color = models.CharField(max_length=30, verbose_name='Цвет')
#     power = models.IntegerField(verbose_name='Мощность')
#     year = models.IntegerField(verbose_name='Год')

#     def __str__(self):
#         return ' '.join([str(self.brand), str(self.model)])

#     class Meta:
#         verbose_name = 'Машина'
#         verbose_name_plural = 'Машины'


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


class Employee(models.Model):
    edu_choises = [('middle', 'среднее'),
                   ('high', 'высшее'),
                   ('professional', 'профессиональное'),
    ]

    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    position = models.CharField(max_length=50,verbose_name='Должность')
    education = models.CharField(max_length=30, choices=edu_choises)

    def __str__(self):
        return ' '.join([str(self.firstname), str(self.lastname)])
    
    def get_absolute_url(self):
        return reverse('main:employee_list')

   
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Car(models.Model):

    colors = (
        ('черный', 'черный'),
        ('белый', 'белый'),
        ('желтый', 'желтый'),
        ('красный', 'красный'),
        ('зеленый', 'зеленый'),
        ('синий', 'синий'),
    )

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=20, choices=colors, null=False)
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год')
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return ' '.join([str(self.brand), str(self.model)])

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, related_name='car', verbose_name='Машина')
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name='driver', verbose_name='Водитель')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='client', verbose_name='Клиент')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([str(self.id), str(self.client)])
    
    def get_absolute_url(self):
        return reverse('main:order_list')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


