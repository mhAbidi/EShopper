from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
import time

# Create your views here.
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