from django.db import models
from datetime import datetime
from django.utils import timezone


class BaseOrderItem(models.Model):
    """
    An item for an order.
    """
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
        
    
    product_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Product name at the moment of purchase.",
    )

    product_code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Product code at the moment of purchase.",
    )

    product = models.ForeignKey(
        "Product",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    _unit_price = models.DecimalField(
        null=True,  # may be NaN
        help_text="Products unit price at the moment of purchase.",
        decimal_places=2, max_digits=20
    )

    _line_total = models.DecimalField(
        null=True,  # may be NaN
        help_text="Line total on the invoice at the moment of purchase.",
        decimal_places=2, max_digits=20
    )

    extra = models.TextField(
        help_text="Arbitrary information for this order item",
    )

    class Meta:
        abstract = True
        verbose_name = "Order item"
        verbose_name_plural = "Order items"

    def __str__(self):
        return self.product_name

    @property
    def unit_price(self):
        return self.order.currency & self._unit_price

    @property
    def line_total(self):
        return self.order.currency & self._line_total

    

    def save(self, *args, **kwargs):
        """
        Before saving the OrderItem object to the database, round the amounts to the given decimal places
        """
        self._unit_price = Order.round_amount(self._unit_price)
        self._line_total = Order.round_amount(self._line_total)
        super(BaseOrderItem, self).save(*args, **kwargs)


STATUS = (
        ('0', 'ACTIVE'),
        ('1', 'DELETED'),
        ('2', 'ARCHIVED'),
        )


class RecordStatusMixin(models.Model):
    class Meta:
        abstract = True

    status = models.CharField(choices=STATUS, max_length=15, default=None)

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(default=datetime.now)
    changed = models.DateTimeField(auto_now=True)

