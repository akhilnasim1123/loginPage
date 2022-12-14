from django.contrib import admin
from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [

    path('home/', views.home, name='home'),
    path('', views.log_in, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),


]
