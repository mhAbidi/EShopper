from django.urls import path
from customerpanel import views

urlpatterns = [
    path('',views.index,name=''),
    path('404',views.nf404,name='404'),
    path('blog',views.blog,name='blog'),
    path('index',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('product-details',views.product_details,name='product-details'),
    path('login', views.login, name='login'),
    path('contact-us',views.contact,name='contact-us'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('logout',views.logout,name="logout"),
    path('404.html',views.nf404,name='404'),
    path('blog.html',views.blog,name='blog'),
    path('index.html',views.index,name='index'),
    path('shop.html',views.shop,name='shop'),
    path('product-details.html',views.product_details,name='product-details'),
    path('login.html', views.login, name='login'),
    path('contact-us.html',views.contact,name='contact-us'),
    path('checkout.html',views.checkout,name='checkout'),
    path('cart.html',views.cart,name='cart'),
    path('logout.html',views.logout,name="logout")

]