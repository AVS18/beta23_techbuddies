from django.shortcuts import render
from .models import SiteAnnouncements
# Create your views here.
def home(request):
    announcement = SiteAnnouncements.objects.all()
    return render(request,"home.html",{'announcement':announcement})