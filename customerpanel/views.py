from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def nf404(request):
    return render(request,'customerpanel/404.html')

def index(request):
    #return HttpResponse("Hello")
    #django.template.loaders.app_directories.Loader: C:\Users\user\Desktop\Neosoft\EShopper\eshopper\adminpanel\templates\customerpanel\404.html (Source does not exist)
    return render(request,'customerpanel/index.html')

def blog(request):
    return HttpResponse("Blog placeholder")

def cart(request):
    return render(request, 'customerpanel/cart.html')


def product_details(request):
    return render(request,'customerpanel/product-details.html')

def login(request):
    return render(request,'customerpanel/login.html')

def shop(request):
    return render(request,'customerpanel/shop.html')

def contact(request):
    return render(request, 'customerpanel/contact-us.html')

def checkout(request):
    return render(request, 'customerpanel/checkout.html')





