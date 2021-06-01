from django.shortcuts import render


def home(request):
    return render(request, 'papercity_app/home.html')


def books(request):
    return render(request, 'papercity_app/books.html')
