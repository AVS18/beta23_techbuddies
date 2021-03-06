from django.shortcuts import render,redirect
from .models import SiteAnnouncements,ContactUs,User,Profile, PlasmaContact
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
            return redirect('/')
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
            place = request.POST["place"]
            User.objects.create_user(first_name=first_name,email=email,phone=phone,user_type=user_type,username=username,password=password,place=place)
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
        try:
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
            messages.info(request,'Profile Updated Successfully')
        except Exception:
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Error Occured Try again later')
            return redirect('/dashboard')
    obj = None
    try:
        obj = Profile.objects.get(person=request.user)
    except:
        obj = None
    if obj is not None:
        return render(request,'saved_profile.html',{'obj':obj})
    else:
        return render(request,'profile.html')
def check_profile_exist(request):
    try:
        return Profile.objects.get(person=request.user)
    except:
        return None
def display(request):
    if request.user.is_authenticated is False:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Login to Continue')
        return redirect('/')
    my_profile, obj = check_profile_exist(request), None
    if my_profile==None:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Update your profile before checking the availability')
        return redirect('/dashboard')
    if request.user.user_type=="Donor":
        if my_profile is not None:
            obj = Profile.objects.filter(person__user_type="Receiver",blood_group=my_profile.blood_group).union(Profile.objects.filter(person__user_type="Receiver",blood_group='O'+my_profile.blood_group[-1]))
            if len(obj)==0:
                storage = messages.get_messages(request)
                storage.used = True
                messages.info(request,'No Donors Available for the request')
                return redirect('/dashboard')
        else:
            obj = Profile.objects.filter(person__user_type="Receiver")
        return render(request,"display_donor.html",{'obj':obj,'places':places()})
    if request.user.user_type=="Receiver":
        if my_profile is not None:
            obj = Profile.objects.filter(person__user_type="Donor",blood_group=my_profile.blood_group).union(Profile.objects.filter(person__user_type="Donor",blood_group='O'+my_profile.blood_group[-1]))
            if len(obj)==0:
                storage = messages.get_messages(request)
                storage.used = True
                messages.info(request,'No Donors Available for the request')
                return redirect('/dashboard')
        else:
            obj = Profile.objects.filter(person__user_type="Donor")
        return render(request,"display_donor.html",{'obj':obj,'places':places()})

def plasma_contact(request,other):
    PlasmaContact.objects.create(requested_by=Profile.objects.filter(person=request.user)[0],requested_to=Profile.objects.get(id=other),status="Pending")
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,'Request Placed Successfully')
    return redirect('/dashboard')

def displayContact(request):
    requests_obtained = PlasmaContact.objects.filter(requested_to__person=request.user)
    requests_made = PlasmaContact.objects.filter(requested_by__person=request.user)
    return render(request,'displayContact.html',{'requests_obtained':requests_obtained,'requests_made':requests_made})

def statusUpdate(request,id,status):
    obj = PlasmaContact.objects.get(id=id)
    obj.status=status
    obj.save()
    if status=="Accepted":
        PlasmaContact.objects.filter(requested_to=obj.requested_by).exclude(id=id).update(status="Rejected")
        PlasmaContact.objects.filter(requested_by=obj.requested_to).exclude(id=id).update(status="Rejected")
        if obj.requested_by.person.user_type=="Donor" and obj.requested_to.person.user_type=="Receiver":
            mail="Greetings\n\nDonor "+obj.requested_by.person.first_name+' Accepted your request and ready to donate plasma.\n\n'
            mail = mail+"Donor Details:\n"+"Name: "+obj.requested_by.person.username+"\n"+"Email ID: "+obj.requested_by.person.email+"\n"
            mail = mail+"Receiver Details:\n"+"Name: "+obj.requested_to.person.username+"\n"+"Email ID: "+obj.requested_to.person.email+"\n"
            mail = mail+"Thank you for the Donation. Keep up this chain to rule out COVID 19 in the world\n\n."
            send_mail("Plasma Request Status",mail,from_email='adityaintern11@gmail.com',recipient_list=[obj.requested_by.person.email,obj.requested_to.person.email])
        elif obj.requested_by.person.user_type=="Receiver" and obj.requested_to.person.user_type=="Donor":
            mail="Greetings\n\nDonor "+obj.requested_to.person.first_name+' Accepted your request and ready to donate plasma.\n\n'
            mail = mail+"Donor Details:\n"+"Name: "+obj.requested_to.person.username+"\n"+"Email ID: "+obj.requested_to.person.email+"\n"
            mail = mail+"Receiver Details:\n"+"Name: "+obj.requested_by.person.username+"\n"+"Email ID: "+obj.requested_by.person.email+"\n"
            mail = mail+"Thank you for the Donation. Keep up this chain to rule out COVID 19 in the world\n\n."
            send_mail("Plasma Request Status",mail,from_email='adityaintern11@gmail.com',recipient_list=[obj.requested_by.person.email,obj.requested_to.person.email])
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,status+" Successfully")
    return redirect('/dashboard')
def places():
    return User.objects.values('place').distinct()
def filter(request):
    place = request.POST["place"]
    my_profile, obj = check_profile_exist(request), None
    if request.user.user_type=="Donor":
        if my_profile is not None:
            obj = Profile.objects.filter(person__user_type="Receiver",blood_group=my_profile.blood_group,person__place=place).union(Profile.objects.filter(person__user_type="Receiver",blood_group='O'+my_profile.blood_group[-1],person__place=place))
            if len(obj)==0:
                storage = messages.get_messages(request)
                storage.used = True
                messages.info(request,'No Donors Available for the request')
                return redirect('/dashboard')
        else:
            obj = Profile.objects.filter(person__user_type="Receiver",person__place=place)
        return render(request,"display_donor.html",{'obj':obj,'places':places()})
    if request.user.user_type=="Receiver":
        if my_profile is not None:
            obj = Profile.objects.filter(person__user_type="Donor",person__place=place,blood_group=my_profile.blood_group).union(Profile.objects.filter(person__user_type="Donor",person__place=place,blood_group='O'+my_profile.blood_group[-1]))
            if len(obj)==0:
                storage = messages.get_messages(request)
                storage.used = True
                messages.info(request,'No Donors Available for the request')
                return redirect('/dashboard')
        else:
            obj = Profile.objects.filter(person__user_type="Donor",person__place=place)
        return render(request,"display_donor.html",{'obj':obj,'places':places()})
