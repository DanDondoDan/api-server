from django.db import models
from api_server.models.customer import Customer
from dummy.exchange_manager.exchange_manager import ExchangeManager


class ExchangeRates(models.Model):

    objects = ExchangeManager()

    CURRENCY_DEFAULT = 'USD'
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    accnumber = models.CharField(max_length=12)
    symbol = models.CharField(max_length=7, default=CURRENCY_DEFAULT)
    rate = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)