from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('home/', views.home, name='home'),
    path("search/", views.Search.as_view(), name="search"),
    path('book_list/', views.BookView.as_view()),
    path('book_list/<slug:slug>', views.BookDetailView.as_view(), name="book_detail"),
    path('categories/<slug:url>/', views.BookView.category_list, name="category_list"),
    path('review/<int:pk>', views.AddReview.as_view(), name="add_review"),
    path('home/selections/selection1', views.selection1, name='selection1'),
    path('home/selections/selection2', views.selection2, name='selection2'),
    path('home/selections/selection3', views.selection3, name='selection3'),
    path('home/selections/selection4', views.selection4, name='selection4'),
    path('home/stocks', views.stocks, name='stocks'),
    path('home/selection_all', views.selection_all, name='selection_all'),
    path('cart/', views.add_to_cart, name='cart'),
    path('get_cart_data/', views.get_cart_data, name='get_cart_data'),
    path('change_quan/', views.change_quan, name='change_quan'),
    path('home/terms', views.terms, name='terms'),


]
