from django.urls import path
from . import views
from django.views.generic import ListView
from .models import Books

urlpatterns = [
    path('',
         ListView.as_view(queryset=Books.objects.all().order_by('-id')[:5], template_name='papercity_app/home.html')),
    path('home', ListView.as_view(queryset=Books.objects.all().order_by('-id')[:5],
                                  template_name='papercity_app/home.html')),
    path('book_list', views.BookView.as_view()),
    path('<slug:url>/', views.BookView.category_list, name="category_list"),
    path('<slug:slug>', views.BookDetailView.as_view(), name="book_detail"),
    path('review/<int:pk>', views.AddReview.as_view(), name="add_review"),

]
