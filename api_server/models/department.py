from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from api_server.models.person import Person
from django.shortcuts import get_object_or_404
from api_server.models.position import Position
from rest_framework.response import Response

class Department(MPTTModel):
    
    id = models.CharField(
        max_length=32,
        primary_key=True,
        unique=True,
        verbose_name='ID',
        help_text='Forsquare ID of the department.',
    )
    name = models.CharField(max_length=255, verbose_name= 'Name')

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        db_index=True,
        verbose_name='Parent department',
        help_text='Parent department.',
        on_delete=models.CASCADE,
    )
    
    plural_name = models.CharField(
        max_length=255,
        verbose_name='Plural name'
    )

    class Meta:
        unique_together = (('parent',))
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def get_person_count(self):
        ids = self.get_descendants(include_self=True)
        return Person.objects.filter(department__in=ids).count()
    
    
    def __str__(self):
        return self.name