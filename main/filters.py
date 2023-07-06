import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    # brand__name = django_filters.CharFilter(label='Марка')
    model = django_filters.CharFilter(field_name='model', lookup_expr='icontains', label='Модель')
    # year = django_filters.NumberFilter(field_name='year', lookup_expr='year')
    # year__gt = django_filters.NumberFilter(field_name='year', lookup_expr='year__gt')
    # year__lt = django_filters.NumberFilter(field_name='year', lookup_expr='year__lt')

    class Meta:
        model = Car
        fields = ['brand', 'model', 'year'] 

        