from django.urls import path, include
from . import views
from django.views.generic import ListView
from .models import Books

urlpatterns = [
    path('', ListView.as_view(queryset=Books.objects.all().order_by('-id')[:5], template_name='papercity_app/home.html')),

]