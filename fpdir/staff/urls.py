from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StaffView.as_view() , name ='staff')
]