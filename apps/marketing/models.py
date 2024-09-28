from django.db import models

# Create your models here.

class Events(models.Model):
    event_code = models.CharField(max_length=20)
    event_name = models.CharField(max_length=300)
    event_image = models.CharField(max_length=400)
    event_start_date = models.CharField(max_length=15)
    estado = models.CharField(max_length=20)
    event_data = models.JSONField(default=dict)
    download_key = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'events'

class Events(models.Model):
    names = models.CharField(max_length=100),
    last_names = models.CharField(max_length=150),
    dni = models.CharField(max_length=15),
    email = models.CharField(max_length=150),
    phone = models.CharField(max_length=15),
    detail = models.JSONField(default=dict)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'events'