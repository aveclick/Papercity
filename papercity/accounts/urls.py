from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profile, name='profile'),
]
