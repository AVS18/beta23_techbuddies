from django.shortcuts import render,redirect
from .models import SiteAnnouncements,ContactUs,User,Profile
from django.contrib import messages,auth
from django.contrib.auth import authenticate
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
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        obj = authenticate(username=username,password=password)
        if obj is not None:
            auth.login(request,obj)
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Login Successful')
        else:
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Please Check your password and try again')
    return redirect('/dashboard')

def register(request):
    if request.method=="POST":
        try:
            first_name=request.POST["first_name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            user_type = request.POST["type"]
            username = request.POST["username"]
            password = request.POST["password"]
            User.objects.create_user(first_name=first_name,email=email,phone=phone,user_type=user_type,username=username,password=password)
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Registration Success')
        except Exception as e:
            print(e)
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Registration Failed. Try again Later')
    return redirect('/')

def logout(request):
    auth.logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,'Logout Successful. Thank you')
    return redirect('/')

def dashboard(request):
    if request.user.is_authenticated is False:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Login to Continue')
        return redirect('/')
    return render(request,'dashboard.html')

def profile(request):
    if request.user.is_authenticated is False:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Login to Continue')
        return redirect('/')
    if request.method=="POST":
        blood_group = request.POST["blood_group"]
        positive_date = request.POST["positive_date"]
        hospital_name = request.POST["hospital_name"]
        uploads = request.FILES
        reports = uploads["report"]
        if request.user.user_type == "Donor":
                negative_date = request.POST["negative_date"]
                vaccinated = request.POST["vaccinated"]
                Profile.objects.create(person=request.user,blood_group=blood_group,positive_date=positive_date,hospital_name=hospital_name,reports=reports,negative_date=negative_date,vaccinated=vaccinated)
        elif request.user.user_type == "Receiver":
                current_health_status = request.POST["current_health_status"]
                no_of_times_tested = request.POST["no_of_times_tested"]
                Profile.objects.create(person=request.user,blood_group=blood_group,positive_date=positive_date,hospital_name=hospital_name,reports=reports,current_health_status=current_health_status,no_of_times_tested=no_of_times_tested)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Error Occured Try again later')
        return redirect('/dashboard')
    return render(request,'profile.html')