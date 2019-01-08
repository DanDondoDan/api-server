from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm




class OrderAdminForm(BaseForm):
    class Meta:
        model = models.Order
        exclude = BaseForm.Meta.exclude


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('created',
                    'closed',
                    'is_closed',
                    'is_processed',
                    'phone',
                    'address',
                    'name',
                    )