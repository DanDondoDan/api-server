from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm
from mptt.admin import MPTTModelAdmin
from api_server.models.department import Department



class DepartmentAdminForm(BaseForm):
    class Meta:
        model = models.Department
        exclude = BaseForm.Meta.exclude


@admin.register(models.Department)
class DepartmentAdmin(MPTTModelAdmin):
    form =  DepartmentAdminForm
    