
from rest_framework.response import Response
from main.price.models import Price
from main.price.api.serializers import PriceSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def PriceViews(request):
    price_list = Price.objects.all()
    price_jsone = PriceSerializer(instance=price_list, many=True).data

    return Response(price_jsone)
