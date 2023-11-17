from django.contrib import admin
from django.urls import path
from main.servicies.api import views

urlpatterns = [
    path('', views.ServiceViews),
]
