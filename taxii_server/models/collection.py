from django.db import models
from django.contrib import admin
from django.db.models.constraints import UniqueConstraint
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.utils.translation import gettext_lazy as _

from taxii_server.models.api_root import ApiRoot

class Collection(models.Model):
    api_root = models.ForeignKey(ApiRoot, related_name='collections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    alias = models.CharField(max_length=100, blank=True)
    media_types = ArrayField(models.CharField(max_length=100), default=list, blank=True)

    class Meta:
        constraints = [UniqueConstraint(fields=['api_root', 'alias'], name='unique_alias_per_api_root')]

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass