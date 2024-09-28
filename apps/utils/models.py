from django.contrib.auth.models import User
from django.db import models

from apps.auth.models import UserProfile


# Create your models here.

class LogSystem(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE),
    area = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    actions = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'log_system'
