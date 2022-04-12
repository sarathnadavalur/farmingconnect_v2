from django.shortcuts import render, redirect
from .models import Retailer
from django.http import HttpResponse

# Create your views here.
def retailers(request):
    retailers = Retailer.objects.all()
    retailer_count = retailers.count
    context = {
        'retailers': retailers,
        'retailer_count' : retailer_count,
    }

    return render(request,'retailers.html', context)