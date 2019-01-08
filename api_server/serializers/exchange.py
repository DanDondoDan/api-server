from rest_framework import serializers
from api_server import models


class ExchangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExchangeRates
        fields = '__all__'
