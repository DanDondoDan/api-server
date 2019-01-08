from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm




class OrderPositionAdminForm(BaseForm):
    class Meta:
        model = models.OrderPosition
        exclude = BaseForm.Meta.exclude


@admin.register(models.OrderPosition)
class OrderPositionAdmin(admin.ModelAdmin):
    form = OrderPositionAdminForm
    list_display = ('order',
                    'product',
                    )