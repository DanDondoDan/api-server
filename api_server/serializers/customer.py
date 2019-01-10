from rest_framework import serializers
from api_server import models

class CustomerSerializer(serializers.ModelSerializer):

    number = serializers.CharField(source='get_number')

    class Meta:
        model = models.Customer
        fields = '__all__'