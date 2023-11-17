
from django.urls import path
from main.vacancies.api import views

urlpatterns = [
    path('', views.VacanciesViews),
]
