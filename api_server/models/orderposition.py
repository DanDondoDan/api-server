from django.db import models

class OrderPosition(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = "Order position"
        verbose_name_plural = "Order Positions"
        ordering = ['-count']

    def price(self):
        return self.product.price * self.count