from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Stock
from ..api.serializers import StockSerializer

@api_view(['GET', 'POST'])
def stock(request):
  if request.method == 'GET':
    stockSerializer = StockSerializer
    stock = Stock.objects.all()
    return Response({"results": stockSerializer(stock, many=True).data })

  if request.method == 'POST':
    serializer = StockSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    stock = Stock()
    try:
      assert request.data['product_id'], "Product_id obrigatório"
      stock.quantity = request.data['quantity']
      stock.product_id = request.data['product_id']
      stock.save()
      return Response(StockSerializer(stock).data, status=status.HTTP_201_CREATED)
    except Exception as error:
      return Response({"message": f'{error}'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET', 'DELETE', 'PUT'])
def stockDetails(request, id):
  try:
    stock = Stock.objects.get(id=id)
  except Stock.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    stockSerializer = StockSerializer
    return Response(stockSerializer(stock).data)
  
  if request.method == 'DELETE':
    stock.delete()
    return Response(status=status.HTTP_200_OK)
  
  if request.method == 'PUT':
    serializer = StockSerializer(stock, data=request.data)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
