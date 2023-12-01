
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('insertUser', insertUser),
    path('home', home, name='home'),
]
