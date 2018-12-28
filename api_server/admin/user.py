from django.contrib import admin
from api_server import models
from api_server.admin.base import BaseForm
import django.forms as forms


class UserAdminForm(BaseForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email', 'password', 'phone', 'birth')


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm