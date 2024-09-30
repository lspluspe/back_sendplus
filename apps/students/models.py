from django.db import models

from apps.auth.models import UserProfile
from apps.courses.models import Courses


# Create your models here.
class CoursesStudents(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    asistence = models.JSONField(null=True)
    notas = models.JSONField(null=True)
    is_active = models.BooleanField(null=True, default=True)
    is_subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'courses_students'