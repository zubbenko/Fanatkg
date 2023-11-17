from rest_framework import generics
from rest_framework.response import Response
from main.servicies.models import Service
from main.servicies.api.serializers import ServiceSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def ServiceViews(request):
    services_list = Service.objects.all()
    services_jsone = ServiceSerializer(instance=services_list, many=True).data

    return Response(services_jsone)


