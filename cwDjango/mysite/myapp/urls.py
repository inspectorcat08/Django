from django.urls import path
from .views import index, first, base


urlpatterns = [
    path('index/', index, name='index'),
    path('first/', first, name='first'),
    path('', base, name='base'),
]