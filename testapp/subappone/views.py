from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

# Create your views here.


def home(request):
    return HttpResponse('Hello World')


def about(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'subappone/about.html', context=context)
