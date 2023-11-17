
from django.urls import path
from main.price.api import views

urlpatterns = [
    path('', views.PriceViews),
]
