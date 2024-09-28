from django.db import models

from apps.auth.models import UserProfile
from apps.courses.models import Courses


# Create your models here.
class Sales(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    detail_cart = models.JSONField(default=dict)
    description = models.JSONField(default=dict)
    type_sales = models.CharField(max_length=20)
    total_price = models.DecimalField(decimal_places=2, max_digits=11, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'sales'

class SalesDetail(models.Model):
    vendedor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    venta = models.ForeignKey('Sales', on_delete=models.CASCADE)
    detail = models.JSONField(default=dict)
    tipo_registro = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'sales_detail'

