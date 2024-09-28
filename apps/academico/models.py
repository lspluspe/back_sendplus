from django.db import models

from apps.auth.models import UserProfile
from apps.courses.models import Modules


# Create your models here.
class ClasesCourses(models.Model):
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    num_class = models.IntegerField()
    detail = models.JSONField(default=dict)
    is_virtual = models.BooleanField(default=True)
    url_class  = models.CharField(max_length=300, null=True, blank=True)
    url_video  = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'clases_courses'

class ClasesCourses(models.Model):
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    num_class = models.IntegerField()
    detail = models.JSONField(default=dict)
    is_virtual = models.BooleanField(default=True)
    url_class  = models.CharField(max_length=300, null=True, blank=True)
    url_video  = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'clases_courses'

class Asistence(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    clase = models.ForeignKey(ClasesCourses, on_delete=models.CASCADE)
    is_estado = models.BooleanField(default=True)
    user_asistence = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    class Meta:
        db_table = 'asistencias'
