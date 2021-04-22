from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nf404(request):
    return render(request,'customerpanel/404.html')

def index(request):
    #return HttpResponse("Hello")
    #django.template.loaders.app_directories.Loader: C:\Users\user\Desktop\Neosoft\EShopper\eshopper\adminpanel\templates\customerpanel\404.html (Source does not exist)
    return render(request,'customerpanel/404.html') 
def home(request):
    return render(request,'customerpanel/404.html')

