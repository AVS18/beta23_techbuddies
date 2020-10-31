from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.BigIntegerField(null=True,blank=True)
    choices = (('Donor','Donor'),('Receiver','Receiver'))
    user_type = models.CharField(choices=choices,max_length=8,null=True,blank=True)
    verification_status = models.BooleanField(default=False)

class SiteAnnouncements(models.Model):
    message = models.CharField(max_length=150)
    link = models.CharField(max_length=50)
    date_announced = models.DateField(auto_now_add=True)

class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.EmailField()
    message=models.CharField(max_length=200)
