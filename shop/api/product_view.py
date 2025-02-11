from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from shop.models.product import Product
from shop.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def by_category(self, request, pk=None):
        products = Product.objects.filter(category_id=pk)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)