from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('books', views.books, name='books'),
    path('cat1', views.cat1, name='cat1'),
    path('cat2', views.cat2, name='cat2'),
    path('cat3', views.cat3, name='cat3'),
    path('cat4', views.cat4, name='cat4'),
    path('cat5', views.cat5, name='cat5'),
    path('cat6', views.cat6, name='cat6'),
    path('cat7', views.cat7, name='cat7'),
    path('cat8', views.cat8, name='cat8'),
    path('cat9', views.cat9, name='cat9'),
]