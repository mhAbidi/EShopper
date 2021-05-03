from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
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
    if request.method == "POST":
        if 'signup' in request.POST:
            first = request.POST["text"]
            email = request.POST["email"]
            password = request.POST["pass"]
            if User.objects.filter(username=first).exists() or User.objects.filter(email=email).exists():
                print("Duiplicate Entry!!")
                messages.info(request,'Duplicate Entry!')
                return redirect("login")
            user = User.objects.create_user(username=first,email=email,password=password)
            user.save();
            print("user added:", first)
            return redirect("/")
        if 'signin' in request.POST:
            first = request.POST["text"]
            password = request.POST["pass"]
            print(first,password)
            user = auth.authenticate(username=first, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
                print("Logged in")
            else:
                messages.info(request,'Invalid credentials')
            return redirect("login")
    else:
        return render(request,'customerpanel/login.html')

def shop(request):
    return render(request,'customerpanel/shop.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def contact(request):
    return render(request, 'customerpanel/contact-us.html')

def checkout(request):
    return render(request, 'customerpanel/checkout.html')





