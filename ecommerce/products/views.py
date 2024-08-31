from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from .models import Producer, Category, Product
from rest_framework.response import Response
# # Create your views here.
# def product(request):
#     return render(request, "products/product.html")

@api_view(['Get'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)