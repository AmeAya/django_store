from django.shortcuts import render, redirect
from .models import *


def homeView(request):  # Каждая view должна принимать request
    categories = Category.objects.all()
    context = {'Categories': categories}
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


def cabinetView(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'GET':
        context = {
            'Customer': customer,
            'Message': 'I am Alive'
        }
        return render(request, 'cabinet.html', context)
    else:  # request.method == 'POST'
        phone = request.POST.get('phone_name')
        username = request.POST.get('username_name')
        if 'photo_name' in request.FILES:
            photo = request.FILES['photo_name']
            customer.photo = photo
        if phone:
            customer.phone = phone
        if username:
            request.user.username = username
            request.user.save()
        customer.save()
        return redirect('cabinet')
