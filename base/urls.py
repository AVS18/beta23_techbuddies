from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('profile',views.profile,name="profile")
]
