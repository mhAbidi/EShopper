from django.urls import path
from adminpanel import views
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

urlpatterns = [
        path('',views.index, name='index'),
        path('/',views.index, name='index'),
        path(r'^',views.index, name='index'),
        path('login', views.login, name='login'),
        path('login.html', views.login, name='login'),
        path('index', views.index, name='index'),
        path('index.html', views.index, name='index')
    ]