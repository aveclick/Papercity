from django.http import request
from django.shortcuts import render


def home(request):
    return render(request, 'papercity_app/home.html')


def books(request):
    return render(request, 'papercity_app/books.html')


def cat1(request):
    return render(request, 'papercity_app/cat1.html')


def cat2(request):
    return render(request, 'papercity_app/cat2.html')


def cat3(request):
    return render(request, 'papercity_app/cat3.html')


def cat4(request):
    return render(request, 'papercity_app/cat4.html')


def cat5(request):
    return render(request, 'papercity_app/cat5.html')


def cat6(request):
    return render(request, 'papercity_app/cat6.html')


def cat7(request):
    return render(request, 'papercity_app/cat7.html')


def cat8(request):
    return render(request, 'papercity_app/cat8.html')


def cat9(request):
    return render(request, 'papercity_app/cat9.html')

