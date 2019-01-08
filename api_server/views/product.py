from rest_framework import viewsets as views
from rest_framework import status
from api_server import models
from api_server import serializers

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import generics
from api_server.decorators.decorators_prod import validate_request_data

 
class SearchProductViewSet(views.ModelViewSet):
    """
    GET product/
    POST product/
    filter/search product/
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    __basic_fields = ('name',
                      'description',
                      'amount',
                      'price',
                      'category',
                      )
    
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET product/:id/
    PUT product/:id/
    DELETE product/:id/
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            pers = self.queryset.get(pk=kwargs["pk"])
            return Response(serializers.ProductSerializer(pers).data)
        except models.Product.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            pers = self.queryset.get(pk=kwargs["pk"])
            serializer = serializers.ProductSerializer
            updated_person = serializer.update(pers, request.data)
            return Response(serializers.ProductSerializer(updated_person).data)
        except models.Product.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            pers = self.queryset.get(pk=kwargs["pk"])
            pers.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Product.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )




    
    