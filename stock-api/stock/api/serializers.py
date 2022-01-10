from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Product, Stock

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'id', 
      'name', 
      'weight', 
      'price', 
      'created_at', 
      'updated_at'
    )

class StockSerializer(serializers.ModelSerializer):
  product = ProductSerializer(many=False, read_only=True)
  
  class Meta:
    model = Stock
    fields = (
      'id', 
      'quantity', 
      'product'
    )
    
  
  def create(self, validated_data):
    return validated_data
  
  def update(self, instance, validated_data):
    instance.quantity = validated_data.get('quantity', instance.quantity)
    return instance