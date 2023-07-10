from django.urls import path
from .views import *


urlpatterns = [
    path('home', homeView, name='home_url'),
]
