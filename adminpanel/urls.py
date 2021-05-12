from django.urls import path
from adminpanel import views
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

urlpatterns = [

        path('',views.index, name='index'),
        path('login', views.login, name='login'),
        path('index', views.index, name='index'),
        path('logout', views.logout,name='logout'),
        path('products', views.products, name='products'),
        path('users',views.users, name='users'),
        path('users_edit/(?P<id>)',views.users_edit, name='users_edit')
    ]