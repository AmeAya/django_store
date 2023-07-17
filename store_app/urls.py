from django.urls import path
from .views import *


urlpatterns = [
    path('home', homeView, name='home_url'),
    path('get_goods_by_category/<int:category_pk>', getGoodsByCategory, name='goods_by_category_url'),
    path('good_detail/<int:good_pk>', goodDetail, name='good_detail'),
    path('cabinet', cabinetView, name='cabinet'),
]
