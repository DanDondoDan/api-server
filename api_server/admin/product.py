from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm




class ProductAdminForm(BaseForm):
    class Meta:
        model = models.Product
        exclude = BaseForm.Meta.exclude


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'description', 'price', 'category', 'active', 'photo', )