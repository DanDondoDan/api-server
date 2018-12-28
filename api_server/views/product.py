from rest_framework import viewsets as views
from rest_framework import status
from api_server import models
from api_server import serializers

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.response import Response


class ProductViewSet(views.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    

class SearchProductViewSet(views.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    __basic_fields = ('name',
                      'category',
                      )
    
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields




    
    