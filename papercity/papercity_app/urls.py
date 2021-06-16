from django.urls import path
from . import views
from django.views.generic import ListView
from .models import Books

urlpatterns = [
    path('', views.home, name=''),
    path('home', views.home, name='home'),
    path("search/", views.Search.as_view(), name="search"),
    path('selection1', views.selection1, name='selection1'),
    path('selection2', views.selection2, name='selection2'),
    path('selection3', views.selection3, name='selection3'),
    path('selection4', views.selection4, name='selection4'),
    path('stocks', views.stocks, name='stocks'),
    path('selection_all', views.selection_all, name='selection_all'),
    path('book_list', views.BookView.as_view()),
    path('<slug:url>/', views.BookView.category_list, name="category_list"),
    path('<slug:slug>', views.BookDetailView.as_view(), name="book_detail"),
    path('review/<int:pk>', views.AddReview.as_view(), name="add_review"),

]
