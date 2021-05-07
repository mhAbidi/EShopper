from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .forms import *
from adminpanel.models import *

import time

# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request, "adminpanel/login.html")

def products(request):
    query_results = Product.objects.all()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Product_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # name = request.POST["your_name"]
            # print(name)
            prod = Product()
            prod.name = request.POST["name"]
            prod.sku = request.POST["sku"]
            prod.short_description = request.POST["short_description"]
            prod.long_description = request.POST["long_description"]
            prod.price = request.POST["price"]
            prod.special_price = request.POST["special_price"]
            prod.quantity = request.POST["quantity"]
            prod.meta_title = request.POST["meta_title"]
            prod.meta_description = request.POST["meta_description"]
            prod.meta_keywords = request.POST["meta_keywords"]
            prod.save();
            messages.success(request,"Successfully added")
            form = Product_Form()
            return render(request, "adminpanel/products.html", {'form':form, 'messages':messages, 'query_results':query_results})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = Product_Form()
    print("find this")
    print(query_results[0])
    return render(request, 'adminpanel/products.html', {'form': form ,'query_results':query_results})

def products_delete(request):


    return redirect("products")


def test(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = Product_Form(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                #name = request.POST["your_name"]
                #print(name)
                prod = Product()
                prod.name = request.POST["name"]
                prod.sku =  request.POST["sku"]
                prod.short_description = request.POST["short_description"]
                prod.long_description = request.POST["long_description"]
                prod.price = request.POST["price"]
                prod.special_price = request.POST["special_price"]
                prod.quantity = request.POST["quantity"]
                prod.meta_title = request.POST["meta_title"]
                prod.meta_description = request.POST["meta_description"]
                prod.meta_keywords =request.POST["meta_keywords"]
                prod.save();

                return HttpResponse("Product Added")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = Product_Form()

        return render(request, 'adminpanel/test.html', {'form': form})


def index(request):
    try:
        if request.user.is_authenticated:
            return render(request,'adminpanel/index.html')
        return render(request, "adminpanel/login.html")
    except:
        return render(request, "adminpanel/login.html")

def login(request):
    if 'user' in request.POST:
        first = request.POST["user"]
        password = request.POST["password"]
        print(first, password)
        user = auth.authenticate(username=first, password=password, is_staff="true" )
        if user is not None:
            auth.login(request, user)
            print("Logged in")
            return redirect("index")
        else:
            messages.info(request, 'Invalid credentials')
        return redirect("login")
    return render(request,'adminpanel/login.html')
