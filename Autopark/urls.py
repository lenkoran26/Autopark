from django.contrib import admin
from django.urls import path, include
from main import urls
from main.views import index, login

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('main/', include(urls)),
    path('login/', login, name='login'),
]
