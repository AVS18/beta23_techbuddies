from django.db import models
from django.contrib.auth.models import AbstractUser
from s3direct.fields import S3DirectField
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

class Profile(models.Model):
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5,choices=(('O+','O+'),('O-','O-'),('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-')))
    positive_date = models.DateField()
    negative_date = models.DateField(blank=True,null=True)
    vaccinated = models.CharField(max_length=5,blank=True,null=True,choices=(("Yes","Yes"),("No","No")))
    current_health_status=models.CharField(max_length=10,blank=True,null=True,choices=(("Normal","Normal"),("Average","Average"),("Critical","Critical")))
    no_of_times_tested = models.IntegerField(default=1)
    reports = models.FileField(upload_to='docs/')
    hospital_name = models.CharField(max_length=200)

class PlasmaContact(models.Model):
    requested_by = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="requested_by")
    requested_to = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="requested_to")
    status = models.CharField(max_length=10,choices=(('Accepted','Accepted'),('Pending','Pending'),('Rejected','Rejected')))