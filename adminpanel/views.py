from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .forms import *
import time

# Create your views here.
def test(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = product(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                #name = request.POST["your_name"]
                #print(name)
                name = request.POST["name"]
                sku =  request.POST["sku"]
                short_description = request.POST["short_description"]
                long_description = request.POST["long_description"]
                price = request.POST["price"]
                special_price = request.POST["special_price"]
                quantity = request.POST["quantity"]
                meta_title = request.POST["meta_title"]
                meta_description = request.POST["meta_description"]
                meta_keywords =request.POST["meta_keywords"]
                send_this = name+"\n"+sku+"\n"+short_description+"\n"+long_description+"\n"+price+"\n"+special_price+"\n"+quantity+"\n"+meta_title+"\n"+meta_description+"\n"+meta_keywords
                return HttpResponse(send_this)

        # if a GET (or any other method) we'll create a blank form
        else:
            form = product()

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
