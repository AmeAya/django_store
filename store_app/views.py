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

    context = {'Customer': customer,
               'Message': 'I am Alive'}
    # context - Данные которые возвращаются на html
    # context обязан быть словарем (dictionary)
    return render(request, 'home.html', context)
