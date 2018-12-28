from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm




class PositionAdminForm(BaseForm):
    class Meta:
        model = models.Position
        exclude = BaseForm.Meta.exclude


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    form = PositionAdminForm
    list_display = ('position', )