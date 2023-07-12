from django.urls import path
from .views import *


urlpatterns = [
    path('home', homeView, name='home_url'),
    path('get_goods_by_category/<int:category_pk>', getGoodsByCategory, name='goods_by_category_url'),
]
