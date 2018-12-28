from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm
from mptt.admin import MPTTModelAdmin
from api_server.models.category import Category



class CategoryAdminForm(BaseForm):
    class Meta:
        model = models.Category
        exclude = BaseForm.Meta.exclude


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    form =  CategoryAdminForm
    