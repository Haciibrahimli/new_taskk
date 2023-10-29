from django.shortcuts import render
from my_app.models import *

def index_view(request):
    my_obj = Category.objects.all()

    context = {
        
    'my_obj':my_obj

    }
    return render(request,'index.html',context)

def contact_view(request):
    my_obj1 = Our_Services.objects.all()

    context = {
        
    'my_obj1':my_obj1

    }
    return render(request,'contact.html',context)


def about_view(request):
    my_obj2 = Our_Services.objects.all()

    context = {
        
    'my_obj2':my_obj2

    }
    return render(request,'about.html',context)


def portfolio_view(request):
    my_obj3 = Our_Services.objects.all()

    context = {
        
    'my_obj3':my_obj3

    }
    return render(request,'portfolio.html',context)

def service_view(request):
    my_obj3 = Our_Services.objects.all()

    context = {
        
    'my_obj3':my_obj3

    }
    return render(request,'service.html',context)
