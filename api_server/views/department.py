from rest_framework import viewsets as views
from api_server import models
from api_server import serializers
# from employee_server.models.subdivision import Subdivision
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import decorators
from rest_framework import generics
from api_server.models.department import Department
from api_server.models.person import Person

from django.shortcuts import get_object_or_404
from oscar.core.loading import get_model
from rest_framework import generics

class DepartmentViewSet(
        mixins.ListModelMixin,
        views.GenericViewSet
    ):
    
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentTreeSerializer
    pagination_class = None

    @decorators.list_route(methods=['get'])
    def tree(self, *args, **kwargs):
    
        categories = Department.objects.filter(level=0).all()
        serializer = serializers.DepartmentTreeSerializer(categories, many=True)
        return Response(data=serializer.data)
        

class DepartmentDetail(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentDetail
  


##############################################################
# Department = get_model('api_server', 'Department')
# Person = get_model('api_server', 'Person')

class DepartmentEmployeerView(generics.ListAPIView):
    serializer_class = serializers.PersonPrivateSerializer

    
    def get_queryset(self):
        sub_id = self.kwargs.get('pk', None)
        if sub_id is not None:
            subdiv = get_object_or_404(Department, id=sub_id)
            return Person.objects.filter(
                unit__in=subdiv.id).all()
        else:
            return Person.objects.none()
    
        
