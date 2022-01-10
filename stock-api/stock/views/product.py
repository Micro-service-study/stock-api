from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Product
from ..api.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def products(request):
  if request.method == 'GET':
    productSerializer = ProductSerializer
    products = Product.objects.all()
    return Response({"results": productSerializer(products, many=True).data })

  if request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
