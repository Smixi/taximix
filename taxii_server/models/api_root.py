from django.core.validators import MinValueValidator
from django.db import models
from django.contrib import admin
from django.contrib.postgres import fields
from django.db.models.fields.related import ForeignKey
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.utils.translation import gettext_lazy as _

class ApiRoot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    versions = ArrayField(models.CharField(blank=False, null=False, max_length=200), default=list)

class State(models.TextChoices):
    FAILURE = 'failure', _('Failure')
    PENDING = 'pending', _('Pending')
    COMPLETE = 'complete', _('Complete')

class ApiRootStatus(models.Model):

    status = models.CharField(max_length=10,choices=State.choices, default=State.PENDING)
    request_timestamp = models.DateTimeField()
    total_count = models.IntegerField(validators=[MinValueValidator(0)])
    api_root = ForeignKey(ApiRoot, on_delete=models.CASCADE, related_name='status')

    @property
    def successes(self):
        details: ApiRootStatusDetail = self.status_details
        return details.filter(state=State.COMPLETE)
    
    @property
    def failures(self):
        details: ApiRootStatusDetail = self.status_details
        return details.filter(state=State.FAILURE)
    
    @property
    def pendings(self):
        details: ApiRootStatusDetail = self.status_details
        return details.filter(state=State.PENDING)

    @property
    def success_count(self):
        return self.successes.count()

    @property
    def failure_count(self):
        return self.failures.count()

    @property
    def pending_count(self):
        return self.pendings.count()
        

class ApiRootStatusDetail(models.Model):
    api_root_status = models.ForeignKey(ApiRootStatus, related_name='status_details', on_delete=models.CASCADE)
    version = models.CharField(max_length=20)
    message = models.TextField()
    state = models.CharField(max_length=10, choices=State.choices, default=State.PENDING)

@admin.register(ApiRoot)
class ApiRootAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass

@admin.register(ApiRootStatus)
class ApiRootStatusAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass

@admin.register(ApiRootStatusDetail)
class ApiRootStatusDetailAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass