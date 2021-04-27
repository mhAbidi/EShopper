"""eshopper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('customerpanel.urls')),
    path('home/',include('customerpanel.urls')),
    path('404/',include('customerpanel.urls')),
    path('index/',include('customerpanel.urls')),
    path('login/',include('customerpanel.urls')),
    path('shop/',include('customerpanel.urls')),
    path('blog/',include('customerpanel.urls')),
    path('product-details/',include('customerpanel.urls')),
    path('contact-us/',include('customerpanel.urls')),
    path('checkout/',include('customerpanel.urls')),
    path('cart/',include('customerpanel.urls')),

    path('adminpanel/', include('adminpanel.urls')),
    path('admin/', admin.site.urls)
]
