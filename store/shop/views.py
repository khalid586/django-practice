from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     #return HttpResponse('hello')
     return render(request,'shop/index.html')