from django.db import models
from api_server.models.base import BaseModel, RecordStatusMixin
from mptt.models import MPTTModel, TreeForeignKey
from api_server.models.position import Position
from api_server.models.profile import Profile
from django.utils import timezone


CHOICE = [('mrs', "Mrs."), ('mr', "Mr."), ('na', "(n/a)")]

class Customer(BaseModel, RecordStatusMixin):

    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                related_name='%(class)s',
                                related_query_name='%(class)s'
                                )
    number = models.PositiveIntegerField(
        null=True,
        default=None,
        unique=True,
        )
    salutation = models.CharField(
        max_length=5,
        choices=CHOICE,
        default='na',
        )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    last_access = models.DateTimeField(
        default=timezone.now,
        )

    photo = models.ImageField(blank=True, null=True, default=None, upload_to='media')
   
    def __str__(self):
        return "{} {} {} {} {} {}({})".format(
            self.number,
            self.salutation,
            self.last_name, 
            self.first_name,
            self.last_access, 
            self.photo, 
            self.user.email
            )

    @classmethod
    def create(cls, user, **kwargs):
        return cls.objects.create(
            user=user,
        )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'

    def get_number(self):
        return self.number

class ProfileCustomer(Profile):
    
    CURRENCY_DEFAULT = 'USD'

    currency = models.CharField(max_length=7, default=CURRENCY_DEFAULT, null=True, blank=True)