from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm


@admin.register(models.IncomeHistory)
class IncomeHistoryAdmin(admin.ModelAdmin):
    pass

class PurchHistoryAdminForm(BaseForm):
    class Meta:
        exclude = BaseForm.Meta.exclude


@admin.register(models.PurchHistory)
class PurchHistoryAdmin(admin.ModelAdmin):
    form = PurchHistoryAdminForm