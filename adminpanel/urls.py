from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.index, name='index')
    
]