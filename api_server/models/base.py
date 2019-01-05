from django.db import models
from datetime import datetime
from django.utils import timezone

STATUS = (
        ('0', 'ACTIVE'),
        ('1', 'DELETED'),
        ('2', 'ARCHIVED'),
        )


class RecordStatusMixin(models.Model):
    class Meta:
        abstract = True

    status = models.CharField(choices=STATUS, max_length=15, default=None)

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(default=datetime.now)
    changed = models.DateTimeField(auto_now=True)