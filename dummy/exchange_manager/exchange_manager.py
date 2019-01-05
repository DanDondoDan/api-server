from django.db import models


class ExchangeManager(models.Manager):
    def create_account(self, symbol, rate):
        account = self.create(symbol=symbol, rate=rate)
        return account