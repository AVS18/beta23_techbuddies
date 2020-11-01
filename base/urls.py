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
    path('profile',views.profile,name="profile"),
    path('display',views.display,name="display"),
    path('plasma_contact/<str:other>',views.plasma_contact,name="plasma_contact"),
    path('displayContact',views.displayContact,name="displayContact"),
    path('statusUpdate/<str:id>/<str:status>',views.statusUpdate,name="statusUpdate"),
    path('filter',views.filter,name="filter")
]
