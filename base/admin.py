from django.contrib import admin
from .models import User, SiteAnnouncements
# Register your models here.
admin.site.register(User)
admin.site.register(SiteAnnouncements)
