from django.urls import path
from . import views

# para ver la iumagen insertada
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.empleados, name='empleados'),
]