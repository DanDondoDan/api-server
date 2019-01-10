from django.db import models
from api_server.models.base import BaseModel


class IncomeHistory(BaseModel):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

class PurchHistory(BaseModel):
    
    STATUSES = (
        ('BOUGHT', 'BOUGHT'),
        ('CANCELLED', 'CANCELLED'),
    )

    status = models.CharField(choices=STATUSES, max_length=100)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


    class Meta:
        ordering = ['-status', 'product',]

    def __str__(self):
        return "{}: ({})".format(self.product.name,
                                    self.status)