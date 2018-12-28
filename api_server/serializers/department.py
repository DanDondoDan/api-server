from rest_framework import serializers
from api_server import models
from rest_framework_recursive.fields import RecursiveField


class DepartmentTreeSerializer(serializers.ModelSerializer):
    
    children = RecursiveField(many=True)
    unit_count = serializers.ReadOnlyField(source='get_person_count')
   

    class Meta:
        model = models.Department
        fields = ('id', 
                  'name',
                  'plural_name',
                  'children',                  
                  'unit_count',
                  )
    
           
class DepartmentDetail(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = ('id', 
                  'name',
                  'plural_name',
                  'children',                  
                  )
    
    
