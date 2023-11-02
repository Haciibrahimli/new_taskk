from django.shortcuts import render
from my_app.models import *
from my_app.forms import ContactForm

def index_view(request):
  

    context = {
        
    }
    return render(request,'index.html',context)

def contact_view(request):
    form = ContactForm()
    
    text = Contact.objects.all()
    services = Our_Services.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            service = form.cleaned_data.get('contact_service')
            form.contact_service = service
            form = ContactForm()
    # service_name = request.POST.get('service')

            
            
    context = {
        'form':form,
        'text':text,
        'services':services,
        
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
    service = request.GET.get('myservice')
    if service is not None:
        services = services.filter(name__icontains=service)
    context = {

    'services':services
    
    }

    return render(request,'service.html',context)

# def maindetails_view(request):

#     context = {

#     }
   

