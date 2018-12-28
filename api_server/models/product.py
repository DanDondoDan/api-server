from django.db import models
from api_server.models.base import BaseModel
from mptt.models import MPTTModel, TreeForeignKey
from api_server.models.position import Position


class Product(BaseModel):

    name = models.CharField(max_length=100)
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    photo = models.ImageField(blank=True, null=True, default=None, upload_to='media/products/')
   
    def __str__(self):
        return "{} {} {}".format(
            self.name, 
            self.category,
            self.photo, 
            )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'