from django.shortcuts import render
from .models import *


def homeView(request):  # Каждая view должна принимать request
    user = request.user  # request.user - это наш user

    # customer = Customer.objects.all()
    # # Выгрузить все данные из таблицы Customer
    # print(customer)
    #
    # customer = Customer.objects.filter(user=user)
    # # Выгрузить записи у которых user это наш user
    # print(customer)

    customer = Customer.objects.get(user=user)
    # Выгрузить только одну запись у которой user это наш user
    # Используйте get когда берем только 1 запись (Желательно по id/pk)
    # print(customer)

    categories = Category.objects.all()
    context = {'Customer': customer,
               'Message': 'I am Alive',
               'Categories': categories}
    # context - Данные которые возвращаются на html
    # context обязан быть словарем (dictionary)
    return render(request, 'home.html', context)


def getGoodsByCategory(request, category_pk):
    goods = Good.objects.filter(category=category_pk)
    context = {'goods': goods}
    return render(request, 'goods_by_category.html', context)


def goodDetail(request, good_pk):
    good = Good.objects.get(pk=good_pk)
    context = {'good': good}
    return render(request, 'good_detail.html', context)
