from rest_framework import generics
from rest_framework.decorators import api_view
from main.vacancies.models import Vacancies
from main.vacancies.api.serializers import VacanciesSerializer
from rest_framework.response import Response

@api_view(['GET'])
def VacanciesViews(request):
    vaca_list = Vacancies.objects.all()
    vaca_json = VacanciesSerializer(instance=vaca_list, many=True).data

    return Response(vaca_json)
    