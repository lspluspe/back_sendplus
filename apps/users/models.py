from django.db import models

from apps.auth.models import UserProfile


# Create your models here.

class UrlPassword(models.Model):
    url_code = models.CharField(max_length=150)
    date_limit = models.CharField(max_length=20)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'url_reset_password'

class NavBar(models.Model):
    is_rol = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    detail = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'nav_bar'

class UserRol(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rol = models.ForeignKey(NavBar, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'nav_bar'