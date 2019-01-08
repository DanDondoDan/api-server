from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm


class ExchangeAdminForm(BaseForm):
    class Meta:
        exclude = BaseForm.Meta.exclude


@admin.register(models.ExchangeRates)
class ExchangeAdmin(admin.ModelAdmin):
    form = ExchangeAdminForm