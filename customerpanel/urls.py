from django.urls import path
from customerpanel import views

urlpatterns = [
    path('', views.home, name='home'),
    path('404',views.nf404, name='nf404')
]