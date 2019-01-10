from rest_framework import serializers
from api_server import models


class ProductSerializer(serializers.ModelSerializer):

    price = serializers.SerializerMethodField()
    availability = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ('name', 'description', 'price', 'category', 'active', 'availability')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', 'catalog')
        super(ProductSerializer, self).__init__(*args, **kwargs)
    

    def get_availability(self, product):
        return product.get_availability(self.context['request'])

class ProductSelectSerializer(serializers.ModelSerializer):
    
    description = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ('id', 'description')

    def get_description(self, instance):
        return instance.product_name

        
        