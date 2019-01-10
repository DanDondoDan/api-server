from django.db import models
from api_server.models.base import BaseModel
from api_server.models.base import BaseOrderItem
from djmoney.models.fields import MoneyField

class Order(BaseModel):
    number = models.PositiveIntegerField(
        null=True,
        default=None,
        unique=True,)
    
    closed = models.DateTimeField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=10, null=True)

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, default=None)

    _subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    _total = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    shipping_address = models.TextField(
        blank=True,
        null=True,
        help_text="Shipping address at the moment of purchase.",
        )

    text = models.TextField(help_text='info fir this order odj on the moment of purshase', default=None)

    currency = models.ForeignKey("ExchangeRates", on_delete=models.CASCADE, default=0)
        

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.get_number()

    def get_number(self):
        """
        Hook to get the order number.
        A class inheriting from Order may transform this into a string which is better readable.
        """
        return str(self.pk)

    @property
    def subtotal(self):
        """
        The summed up amount for all ordered items excluding extra order lines.
        """
        return self.currency & self._subtotal

    @property
    def total(self):
        """
        The final total to charge for this order.
        """
        return self.currency & self._subtotal

class OrderPayment(BaseModel):
    """
    A model to hold received payments for a given order.
    """
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
        

    amount = MoneyField(decimal_places=2, max_digits=20)
        

    transaction_id = models.CharField(
        max_length=255,
        help_text="The transaction processor's reference",
    )

    payment_method = models.CharField(
        max_length=50,
        help_text="The payment backend used to process the purchase",
    )

    class Meta:
        verbose_name = "Order payment"
        verbose_name_plural = "Order payments"

    def __str__(self):
        return "Payment ID: {}".format(self.id)

class OrderItem(BaseOrderItem):
    """Default materialized model for OrderItem"""
    quantity = models.IntegerField("Ordered quantity")


