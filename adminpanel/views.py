from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .forms import *
from adminpanel.models import *

import time

# Create your views here.
def logout(request):
    auth.logout(request)
    return login(request)


def users_edit(request,id):
    print(id)
    context={}
    obj = get_object_or_404(Users, id=id)
    form = User_Form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        print("this happened!!!")
        return render(request,"adminpanel/users.html")


    context["form"]=form
    return render(request,"adminpanel/users_edit.html",{'form':form})




def users(request):
    query_results = Users.objects.all()
    if request.method == 'POST':
        try:
            delete_request = request.POST["delete"]
            if delete_request == "yes":
                print("i am here")
                id = request.POST["id"]
                user = Users.objects.filter(id=id)
                user.delete();
                print(id)
                request.POST["delete"] = "no"
                return render(request,"adminpanel/users.html")
        except: pass
        form = User_Form(request.POST)
        if form.is_valid():
            user = Users()
            user.firstname = request.POST["firstname"]
            user.lastname = request.POST["lastname"]
            user.email = request.POST["email"]
            user.password = request.POST["password"]
            user.is_staff = True
            user.status = True
            user.save();
            messages.success(request, "Successfully added")
            form = User_Form()
            return render(request, "adminpanel/users.html",
                          {'form': form, 'messages': messages, 'query_results': query_results})
    else:
        form = User_Form()
    return render(request, 'adminpanel/users.html', {'form': form, 'query_results': query_results})

def products(request):
    query_results = Product.objects.all()

    if request.method == 'POST':
        form = Product_Form(request.POST)
        if form.is_valid():
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
    else:
        form = Product_Form()
    return render(request, 'adminpanel/products.html', {'form': form ,'query_results':query_results})

def products_delete(request):


    return redirect("products")


def index(request):
    try:
        if request.user.is_authenticated:
            return render(request,'adminpanel/index.html')
        return login(request)
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
            return redirect("")
        else:

            messages.add_message(request, messages.INFO, "Invalid Credentials")
        return render(request, "adminpanel/login.html")

    return render(request, "adminpanel/login.html")
