from main.price.models import Price
from rest_framework import serializers

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricefields = '__all__'


