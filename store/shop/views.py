from django.shortcuts import render
from .models import Product

# Create your views here.
from django.http import HttpResponse

def index(request):
    prod = Product.objects.all()
    return render(request, 'shop/index.html',{'products':prod})

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")
