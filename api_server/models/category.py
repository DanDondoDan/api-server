from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from api_server.models.product import Product
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class Category(MPTTModel):
    
    id = models.CharField(
        max_length=32,
        primary_key=True,
        unique=True,
        verbose_name='ID',
        help_text='Forsquare ID of the category.',
    )
    name = models.CharField(max_length=255, verbose_name= 'Name')

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        db_index=True,
        verbose_name='Parent category',
        help_text='Parent category.',
        on_delete=models.CASCADE,
    )
    
    plural_name = models.CharField(
        max_length=255,
        verbose_name='Plural name'
    )

    class Meta:
        unique_together = (('parent',))
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def get_product_count(self):
        ids = self.get_descendants(include_self=True)
        return Product.objects.filter(category__in=ids).count()
    
    
    def __str__(self):
        return self.name