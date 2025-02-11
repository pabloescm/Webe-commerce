from django.db import models
from .product import Product

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"Image for {self.product.name}"