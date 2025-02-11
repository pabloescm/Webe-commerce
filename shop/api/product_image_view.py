from rest_framework import viewsets
from shop.models.product_image import ProductImage
from shop.serializers import ProductImageSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer