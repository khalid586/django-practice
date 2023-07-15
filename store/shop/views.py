from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     return render(request,'shop/index.html')

def about(request):
     return HttpResponse('we are at about')

def contact(request):
     return HttpResponse('we are at contact')

def checkout(request):
     return HttpResponse('we are at checkout')