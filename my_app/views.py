from django.shortcuts import render
from my_app.models import *
from my_app.forms import *

def index_view(request):


    context = {
        
    }
    return render(request,'index.html',context)

def contact_view(request):
    form = ContactForm()
    
    text = Contact.objects.all()

    context = {
        'form':form,
        'text':text,
        
    }
    return render(request,'contact.html',context)


def about_view(request):
    title = About.objects.all()

    context = {      
        'title':title
    }
    return render(request,'about.html',context)


def portfolio_view(request):

    images = Portfolio.objects.all()
    
  
    context = {

       'images': images 

    }
    return render(request,'portfolio.html',context)

def service_view(request):
    services = Our_Services.objects.all()
    context = {

    'services':services
    
    }

    return render(request,'service.html',context)

# def maindetails_view(request):

#     context = {

#     }
   

