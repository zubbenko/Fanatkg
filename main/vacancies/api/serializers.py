from main.vacancies.models import Vacancies
from rest_framework import serializers

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'

