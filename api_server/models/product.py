from django.db import models
from api_server.models.base import BaseModel
from mptt.models import MPTTModel, TreeForeignKey
from api_server.models.position import Position


class Product(BaseModel):

    name = models.CharField(max_length=100)
    # unit = TreeForeignKey('Unit', null=True, blank=True, on_delete=models.CASCADE)

    photo = models.ImageField(blank=True, null=True, default=None, upload_to='media')
   
    def __str__(self):
        return "{} {} {}".format(
            self.name, 
            self.unit,
            self.photo, 
            )

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'