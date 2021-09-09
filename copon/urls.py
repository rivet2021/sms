
from django.urls import path,include
from .import views

urlpatterns = [
  path('home/', views.home,name="home"),
    path('sms/', views.sendsms,name="sendsms"),
    path('smsdone/', views.smsdone,name="smsdone"),

    

    ]
