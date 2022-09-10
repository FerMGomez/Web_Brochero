from django.contrib import admin
from django.urls import path
from Brochero_web.view import inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',inicio),
]
