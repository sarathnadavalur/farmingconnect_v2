from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product


def home(request):

    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
        'loop_count' : range(0, 8),
    }
    return render(request,'home.html', context)