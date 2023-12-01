
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('insertUser', insertUser),
    path('home', home, name='home'),
    path('phone', phone, name='phone'),
    path('message', message, name='message'),
]
