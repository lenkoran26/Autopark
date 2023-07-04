from django.contrib import admin
from django.urls import path, include
from main import urls as main_urls
from users import urls as users_urls
from main.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('main/', include(main_urls)),
    path('users/', include(users_urls)),
]
