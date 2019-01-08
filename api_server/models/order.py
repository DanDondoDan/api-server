from django.db import models

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def price(self):
        total_price = 0
        
        for p in self.positions.all():
            total_price += p.price()

        return total_price