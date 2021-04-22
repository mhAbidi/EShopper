from django.urls import path
from customerpanel import views

urlpatterns = [
    path('',views.nf404,name='404')
]