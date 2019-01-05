from django.db import models
from .base import BaseModel



class Profile(BaseModel):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='%(class)s',
        related_query_name='%(class)s')

    class Meta:
        abstract = True

    def __str__(self):
        return '{} ({})'.format(self.user.full_name, self.user.email)

    @classmethod
    def create(cls, user):
        return cls.objects.create(
            user=user,
        )