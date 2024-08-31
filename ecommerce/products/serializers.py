from rest_framework import serializers
from .models import Producer, Product, Category

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['id', 'producer_name']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'cat_name']
        
class ProductSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()
    Category_name = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'