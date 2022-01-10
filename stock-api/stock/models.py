from django.db import models
from uuid import uuid4

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=255)
  weight = models.FloatField()
  price = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
class Stock(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  quantity = models.IntegerField()
  product = models.OneToOneField(Product, related_name='product', on_delete=models.CASCADE, unique=True)
  
  class Meta:
    ordering = ['-quantity']