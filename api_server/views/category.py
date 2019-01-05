from rest_framework import viewsets as views
from api_server import models
from api_server import serializers
# from employee_server.models.subdivision import Subdivision
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import decorators
from rest_framework import generics
from api_server.models.category import Category
from api_server.models.product import Product

from django.shortcuts import get_object_or_404
from oscar.core.loading import get_model
from rest_framework import generics

class CategoryViewSet(
        mixins.ListModelMixin,
        views.GenericViewSet
    ):
    
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryTreeSerializer
    pagination_class = None

    @decorators.list_route(methods=['get'])
    def tree(self, *args, **kwargs):
    
        categories = Category.objects.filter(level=0).all()
        serializer = serializers.CategoryTreeSerializer(categories, many=True)
        return Response(data=serializer.data)
        

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryDetail
  


class CategoryProductView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    
    def get_queryset(self):
        sub_id = self.kwargs.get('pk', None)
        if sub_id is not None:
            subdiv = get_object_or_404(Category, id=sub_id)
            return Product.objects.filter(
                unit__in=subdiv.id).all()
        else:
            return Product.objects.none()
    
        
