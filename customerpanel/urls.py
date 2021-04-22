from django.urls import path
from customerpanel import views

urlpatterns = [
    path('', views.home, name='404'),
    path('404',views.nf404, name='404'),
    path('index',views.index,name='index'),

]