from django.shortcuts import render,redirect
from .models import SiteAnnouncements,ContactUs
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request):
    announcement = SiteAnnouncements.objects.all()
    return render(request,"home.html",{'announcement':announcement})

def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        obj = ContactUs.objects.create(name=name,phone=phone,email=email,message=message)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Thank you for Joining with us. You will receive a notification soon')
        msg = 'Mr. '+name+',\n\n\tThank you for joining with our Team. We will contact you soon'
        try:
            send_mail("Let's Donate Volunteer",msg,from_email='adityaintern11@gmail.com',recipient_list=[email])
        except Exception:
            messages.info(request,'Wrong Email Credentails Delivered.')
    return redirect('/')

def login(request):
    #todo
    return redirect('/')

def register(request):
    #todo
    return redirect('/')

def logout(request):
    #todo
    return redirect('/')
