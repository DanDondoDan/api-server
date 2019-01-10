from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm




class CustomerAdminForm(BaseForm):
    class Meta:
        model = models.Customer
        exclude = BaseForm.Meta.exclude


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = (
                    'number',
                    'salutation',
                    'last_name',
                    'first_name',
                    'last_access',
                    'photo',
                    )

class ProfileCustomerAdminForm(BaseForm):
    class Meta:
        model = models.ProfileCustomer
        exclude = BaseForm.Meta.exclude


@admin.register(models.ProfileCustomer)
class ProfileCustomerAdmin(admin.ModelAdmin):
    form = ProfileCustomerAdminForm