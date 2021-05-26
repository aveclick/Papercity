from django.shortcuts import render


def home(request):
    return render(request, 'papercity_app/home.html')