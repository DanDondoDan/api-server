from rest_framework import serializers
from api_server import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ('name',
                  'amount',
                  'price',
                  'category',
                  'photo',
                  )

        
        