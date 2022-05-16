from django.contrib.auth import get_user_model
from django.shortcuts import render
from products.models import Product, Category


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products/home.html', {'categories': categories, 'products': products})


def discount(request):
    discounts = Product.objects.filter(is_discount=True).all()
    return render(request, 'products/products_list.html', {'products': discounts})


def new_arrive(request):
    new_arrives = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': new_arrives})


def delivery_info(request):
    return render(request, 'products/delivery_info.html')


def payment_info(request):
    return render(request, 'products/payment_info.html')


def return_info(request):
    return render(request, 'products/return_info.html')
