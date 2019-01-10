from django.db import models
from api_server.models.base import BaseModel
from mptt.models import MPTTModel, TreeForeignKey
from api_server.models.position import Position


class Product(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    photo = models.ImageField(blank=True, null=True, default=None, upload_to='media/products/')
    active = models.BooleanField(
        default=True,
        help_text="Is this product publicly visible.",
        )
    def __str__(self):
        return "{} {} {} {} {} {} ".format(
            self.name,
            self.description,
            self.price, 
            self.category,
            self.active,
            self.photo, 
            )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
    