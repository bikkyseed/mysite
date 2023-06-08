from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('admit',views.admit,name='admit'),
    path('about/',views.about,name='about'),
    path('search',views.search,name='search'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('logout',views.handleLogout,name='handleLogout'),
    path('tool/',views.tool,name='tool'),
    

]