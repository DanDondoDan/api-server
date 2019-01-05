from django.db import models
from api_server.models.base import BaseModel, RecordStatusMixin
from mptt.models import MPTTModel, TreeForeignKey
from api_server.models.position import Position


class Customer(BaseModel, RecordStatusMixin):

    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                related_name='%(class)s',
                                related_query_name='%(class)s'
                                )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    photo = models.ImageField(blank=True, null=True, default=None, upload_to='media')
   
    def __str__(self):
        return "{} {} {} ({})".format(
            self.last_name, 
            self.first_name, 
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