from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/<str:id>/', contacts, name='contacts'),
    
    path('cars/<int:pk>/', car_detail, name='car_detail'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('clients/', clients, name='clients'),
    
    path('add_car/', add_car, name='add_car'),
    path('add_driver/', add_driver, name='add_driver'),
    path('add_client/', add_client, name='add_client'),
    
    path('employees/<int:pk>/update/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDelete.as_view(), name='employee-delete'), 
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('employee_form/', EmployeeCreate.as_view(), name='employee-form'),
    
]