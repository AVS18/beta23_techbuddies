from django.contrib import admin
from .models import User, SiteAnnouncements,Profile
# Register your models here.
admin.site.register(User)
admin.site.register(SiteAnnouncements)
admin.site.register(Profile)