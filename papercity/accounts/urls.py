from django.urls import path
from . import views
from django.views.generic import ListView
from django.conf.urls import url
from papercity_app.models import Books

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    url(r'^profile/$', views.edit, name='profile'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    url(r'^password/$', views.change_password, name='change_password'),
]

