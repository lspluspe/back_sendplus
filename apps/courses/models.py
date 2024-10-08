from django.db import models

from apps.auth.models import UserProfile


# Create your models here.

class Modalidad(models.Model):
    name = models.CharField(max_length=150)
    tag = models.CharField(max_length=20)
    detail = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'tipo_modalidad'

class Ciclo(models.Model):
    name = models.CharField(max_length=150)
    tag = models.CharField(max_length=20)
    detail = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'cicle_course'

class CoursesNames(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    information = models.JSONField(default=dict)

    class Meta:
        db_table = 'courses_names'

class CourseDetail(models.Model):
    name = models.CharField(max_length=255)
    ciclo = models.ForeignKey('Ciclo', on_delete=models.CASCADE)
    tipo_modalidad = models.ForeignKey('Modalidad', on_delete=models.CASCADE)
    courses_name = models.ForeignKey('CoursesNames', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    information = models.JSONField(default=dict)

    class Meta:
        db_table = 'courses_detail'

class Courses(models.Model):

    name = models.CharField(max_length=200)
    courses_code = models.CharField(max_length=20)
    start_date = models.CharField(max_length=40)
    limit_students = models.IntegerField()
    detail = models.JSONField(default=dict)
    number_group = models.IntegerField()
    course_detail =  models.ForeignKey('CourseDetail', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'course'



class Modules(models.Model):
    module_name = models.CharField(max_length=255)
    module_number = models.IntegerField(null=True)
    module_description = models.CharField(max_length=400, null=True)
    module_detail = models.JSONField()
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'modules'



