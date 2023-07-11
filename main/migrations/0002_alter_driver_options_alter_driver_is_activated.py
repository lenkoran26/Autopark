# Generated by Django 4.2.3 on 2023-07-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Водитель', 'verbose_name_plural': 'Водители'},
        ),
        migrations.AlterField(
            model_name='driver',
            name='is_activated',
            field=models.BooleanField(default=True, verbose_name='Активация'),
        ),
    ]
