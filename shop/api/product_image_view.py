from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from shop.models.product_image import ProductImage
from shop.serializers import ProductImageSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    @action(detail=True, methods=['get'], url_path='images')
    def get_images(self, request, pk=None):
        images = ProductImage.objects.filter(product_id=pk)
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)