from rest_framework import serializers
from api_server import models
from rest_framework_recursive.fields import RecursiveField


class CategoryTreeSerializer(serializers.ModelSerializer):
    
    children = RecursiveField(many=True)
    category_count = serializers.ReadOnlyField(source='get_product_count')
   

    class Meta:
        model = models.Category
        fields = ('id', 
                  'name',
                  'plural_name',
                  'children',                  
                  'category_count',
                  )

    
           
class CategoryDetail(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id', 
                  'name',
                  'plural_name',
                  'children',                  
                  )
    
    
